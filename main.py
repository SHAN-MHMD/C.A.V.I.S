import speech_recognition as sr
import pyttsx3

from clap_detector import wait_for_clap
from actions import open_app


# ==========================================
# INITIALIZATION
# ==========================================

recognizer = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty(
    "rate",
    175
)

engine.setProperty(
    "volume",
    1.0
)


# ==========================================
# SPEAK
# ==========================================

def speak(text):

    print("CAVIS:", text)

    engine.say(text)

    engine.runAndWait()


# ==========================================
# LISTEN
# ==========================================

def listen_command():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

        except sr.WaitTimeoutError:

            return None


    try:

        command = recognizer.recognize_google(
            audio
        ).lower().strip()

        print("You:", command)

        return command


    except sr.UnknownValueError:

        print("Couldn't understand.")

        return None


    except sr.RequestError:

        speak(
            "Speech recognition service "
            "is unavailable."
        )

        return None


# ==========================================
# MAIN CAVIS LOOP
# ==========================================

def main():

    print()
    print("=" * 45)
    print("        C.A.V.I.S")
    print("  Clap Activated Voice Instructive Software")
    print("=" * 45)
    print()


    speak(
        "CAVIS is ready."
    )


    while True:

        # ----------------------------------
        # WAIT FOR CLAP
        # ----------------------------------

        clap_detected = wait_for_clap()


        if not clap_detected:

            speak(
                "Clap detection stopped."
            )

            break


        print(
            "👏 CAVIS ACTIVATED"
        )


        # ----------------------------------
        # LISTEN FOR COMMAND
        # ----------------------------------

        command = listen_command()


        if not command:

            print(
                "No command detected."
            )

            continue


        # ----------------------------------
        # DEACTIVATE
        # ----------------------------------

        if (
            "deactivate" in command
            or "no more needed" in command
            or "shutdown" in command
            or "stop" in command
            or "exit" in command
            or "quit" in command
        ):

            speak(
                "CAVIS is going offline."
            )

            break


        # ----------------------------------
        # REMOVE CAVIS FROM COMMAND
        # ----------------------------------

        command = command.replace(
            "cavis",
            ""
        ).strip()


        if not command:

            speak(
                "Please give me a command."
            )

            continue


        # ----------------------------------
        # EXECUTE
        # ----------------------------------

        response = open_app(
            command
        )


        speak(
            response
        )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":

    main()