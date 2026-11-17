import sounddevice as sd
import numpy as np
import time


# ==========================================
# CAVIS CLAP DETECTOR
# ==========================================

SAMPLE_RATE = 44100
BLOCK_SIZE = 1024

# Sensitivity
MIN_RMS = 0.035
RMS_MULTIPLIER = 10.0

# Clap characteristics
MIN_CREST_FACTOR = 3.0
MIN_HIGH_FREQ_RATIO = 0.25

# Prevent repeated detection
COOLDOWN = 1.0


def wait_for_clap():

    baseline = 0.01
    last_clap = 0

    detected = False

    def audio_callback(indata, frames, time_info, status):

        nonlocal baseline
        nonlocal last_clap
        nonlocal detected

        if detected:
            return

        audio = indata[:, 0].astype(np.float32)

        # --------------------------------------
        # 1. RMS / average volume
        # --------------------------------------

        rms = np.sqrt(
            np.mean(audio ** 2)
        )

        # --------------------------------------
        # 2. Peak volume
        # --------------------------------------

        peak = np.max(
            np.abs(audio)
        )

        # --------------------------------------
        # 3. Crest factor
        # Sharp sounds have a high value
        # --------------------------------------

        crest_factor = (
            peak / max(rms, 0.00001)
        )

        # --------------------------------------
        # 4. Learn background noise slowly
        # --------------------------------------

        if rms < baseline * 2.0:

            baseline = (
                baseline * 0.98
                + rms * 0.02
            )

        threshold = max(
            MIN_RMS,
            baseline * RMS_MULTIPLIER
        )

        # --------------------------------------
        # 5. Frequency analysis
        # --------------------------------------

        window = np.hanning(len(audio))

        spectrum = np.abs(
            np.fft.rfft(
                audio * window
            )
        )

        frequencies = np.fft.rfftfreq(
            len(audio),
            1 / SAMPLE_RATE
        )

        total_energy = np.sum(
            spectrum
        )

        if total_energy <= 0:

            return

        # Energy above 2 kHz
        high_frequency_energy = np.sum(
            spectrum[frequencies >= 2000]
        )

        high_frequency_ratio = (
            high_frequency_energy
            / total_energy
        )

        # --------------------------------------
        # 6. Current time
        # --------------------------------------

        current_time = time.time()

        cooldown_finished = (
            current_time - last_clap
            > COOLDOWN
        )

        # --------------------------------------
        # 7. Clap decision
        # --------------------------------------

        loud_enough = (
            rms > threshold
        )

        sharp_enough = (
            crest_factor >= MIN_CREST_FACTOR
        )

        high_frequency_enough = (
            high_frequency_ratio
            >= MIN_HIGH_FREQ_RATIO
        )

        if (
            loud_enough
            and sharp_enough
            and high_frequency_enough
            and cooldown_finished
        ):

            last_clap = current_time
            detected = True

            print()
            print("👏 CLAP DETECTED!")
            print(
                f"   RMS: {rms:.3f}"
            )
            print(
                f"   Crest: {crest_factor:.2f}"
            )
            print(
                f"   High-frequency: "
                f"{high_frequency_ratio:.2f}"
            )


    # ==========================================
    # START MICROPHONE
    # ==========================================

    print()
    print("================================")
    print("       CAVIS CLAP DETECTOR")
    print("================================")
    print()
    print("😴 Waiting for clap...")


    try:

        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            blocksize=BLOCK_SIZE,
            channels=1,
            dtype="float32",
            callback=audio_callback
        ):

            while not detected:

                time.sleep(0.05)


    except KeyboardInterrupt:

        print()
        print("Clap detector stopped.")

        return False


    except Exception as error:

        print()
        print("Microphone error:")
        print(error)

        return False


    return True