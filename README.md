# C.A.V.I.S. – Clap Activated Voice Instructive Software

A Python-based desktop assistant that lets users control their desktop environment using **clap detection and voice commands**.

C.A.V.I.S. listens for a clap, activates voice recognition, and performs the requested action — such as opening applications, accessing websites, or launching predefined productivity modes.

## ✨ Features

- **Clap Activation:** Activates voice recognition when a clap is detected.
- **Voice Commands:** Recognizes spoken commands to perform actions.
- **Application Launcher:** Quickly opens applications such as Google Chrome and Visual Studio Code.
- **Website Launcher:** Opens frequently used websites such as YouTube, Google, GitHub, ChatGPT, Instagram, WhatsApp, and Netflix.
- **Productivity Modes:** Launches multiple applications with a single command.

### Available Modes

| Mode | Actions |
|---|---|
| Coding Mode | Opens Visual Studio Code and ChatGPT |
| Study Mode | Opens Visual Studio Code, Documents, and ChatGPT |
| Entertainment Mode | Opens Netflix and YouTube |

## 🛠️ Technologies Used

- **Python 3.10**
- SpeechRecognition – Voice command recognition
- PyAudio – Microphone input
- pyttsx3 – Text-to-speech responses
- SoundDevice – Audio input processing
- NumPy – Audio signal analysis

## 📁 Project Structure

```text
CAVIS/
│
├── main.py             # Main application and voice assistant loop
├── clap_detector.py    # Detects clap sounds
├── actions.py          # Handles application and website launching
├── config.py           # Application paths and configuration
└── requirements.txt    # Project dependencies
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/CAVIS.git
```

### 2. Navigate to the project directory

```bash
cd CAVIS
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure application paths

Open `config.py` and update the application paths according to your system.

### 6. Run C.A.V.I.S.

```bash
python main.py
```

## 🎙️ How to Use

1. Run the application.
2. Wait for C.A.V.I.S. to announce that it is ready.
3. Clap your hands to activate voice recognition.
4. Speak a supported command.
5. C.A.V.I.S. executes the requested action and waits for the next clap.

To stop the assistant, say:

**"Deactivate CAVIS"**

## 💻 Example Voice Commands

- "Open Chrome"
- "Open Visual Studio Code"
- "Open YouTube"
- "Open GitHub"
- "Open ChatGPT"
- "Activate Coding Mode"
- "Activate Study Mode"
- "Activate Entertainment Mode"
- "Deactivate CAVIS"

## 📌 Requirements

- Windows operating system
- Python 3.10 or compatible version
- Working microphone
- Internet connection for online speech recognition
- Required applications installed on your computer

## 🔮 Future Improvements

- More accurate clap detection in different environments.
- Support for customizable voice commands.
- Additional productivity modes.
- Improved voice recognition and command handling.
- User-configurable application shortcuts.

## 👨‍💻 Developer

Developed as a Python desktop automation project to explore audio processing, speech recognition, and application control.

---

**C.A.V.I.S. – Clap. Speak. Execute.**
