import subprocess
import webbrowser
import os

import config


# ==========================================
# APPLICATIONS
# ==========================================

def open_chrome():

    if not os.path.exists(config.CHROME):

        return "Chrome was not found."

    subprocess.Popen(config.CHROME)

    return "Opening Chrome."


def open_vscode():

    if not os.path.exists(config.VSCODE):

        return "VS Code was not found."

    subprocess.Popen(config.VSCODE)

    return "Opening VS Code."


def open_files():

    if not os.path.exists(config.FILES):

        return "The files folder was not found."

    os.startfile(config.FILES)

    return "Opening Files."


# ==========================================
# WEBSITES
# ==========================================

def open_youtube():

    webbrowser.open(
        "https://www.youtube.com"
    )

    return "Opening YouTube."


def open_google():

    webbrowser.open(
        "https://www.google.com"
    )

    return "Opening Google."


def open_github():

    webbrowser.open(
        "https://github.com"
    )

    return "Opening GitHub."


def open_chatgpt():

    webbrowser.open(
        "https://chatgpt.com"
    )

    return "Opening ChatGPT."


def open_instagram():

    webbrowser.open(
        "https://www.instagram.com"
    )

    return "Opening Instagram."


def open_whatsapp():

    webbrowser.open(
        "https://web.whatsapp.com"
    )

    return "Opening WhatsApp."


def open_netflix():

    webbrowser.open(
        "https://www.netflix.com"
    )

    return "Opening Netflix."


# ==========================================
# CODING MODE
# ==========================================

def coding_mode():

    vscode_result = open_vscode()

    webbrowser.open(
        "https://chatgpt.com"
    )

    return "Initiating Coding Mode."


# ==========================================
# STUDY MODE
# ==========================================

def study_mode():

    open_vscode()

    open_files()

    webbrowser.open(
        "https://chatgpt.com"
    )

    return "Initiating Study Mode."


# ==========================================
# ENTERTAINMENT MODE
# ==========================================

def entertainment_mode():

    open_netflix()

    webbrowser.open(
        "https://www.youtube.com"
    )

    return "Initiating Entertainment Mode."


# ==========================================
# COMMAND HANDLER
# ==========================================

def open_app(command):

    command = command.lower().strip()


    # --------------------------------------
    # MODES FIRST
    # --------------------------------------

    if "coding mode" in command:

        return coding_mode()


    elif "study mode" in command:

        return study_mode()


    elif "entertainment mode" in command:

        return entertainment_mode()


    # --------------------------------------
    # APPLICATIONS
    # --------------------------------------

    elif "vs code" in command:

        return open_vscode()


    elif "visual studio code" in command:

        return open_vscode()


    elif "chrome" in command:

        return open_chrome()


    elif "files" in command:

        return open_files()


    # --------------------------------------
    # WEBSITES
    # --------------------------------------

    elif "youtube" in command:

        return open_youtube()


    elif "google" in command:

        return open_google()


    elif "github" in command:

        return open_github()


    elif "chat gpt" in command:

        return open_chatgpt()


    elif "instagram" in command:

        return open_instagram()


    elif "whatsapp" in command:

        return open_whatsapp()


    elif "netflix" in command:

        return open_netflix()


    # --------------------------------------
    # UNKNOWN
    # --------------------------------------

    return (
        "I don't know that application "
        "or website yet."
    )