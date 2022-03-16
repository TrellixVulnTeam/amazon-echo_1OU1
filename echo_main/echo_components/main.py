"""
GUI & Controller
======================
Runs Amazon Echo
------------------------
Runs Amazon Echo program
...........................

"""

from tkinter import CENTER, Tk, Button
from listening_service import record
from speech_to_txt import speech_to_text
from database_retriv import retrieve_file
from txt_to_speech import text_to_speech
from answer_service import answer_mode
import threading
import logging
import sys

# beginning and middleware for echo application

logging.basicConfig(level=logging.DEBUG)
Mode = True


def controller() -> None:
    """A directional services for speech
    if user requests play, passess to pass rel functions
    if user asks a questions pass to rel function to handle
    """
    while Mode:
        my_gui.configure(background='cyan')
        logging.debug("Listening...")
        record()
        x = speech_to_text()
        if x is None and Mode is False:
            logging.debug("Pausing Program")
            my_gui.configure(background='grey')
        elif x is None:
            logging.debug("no request given")
        elif "play" in x:
            requested = x.replace('play', '').replace('.', '').lower().strip()
            my_gui.configure(background='green')
            logging.debug("changing background color")
            retrieve_file(requested)
        else:
            question_asked = x
            my_gui.configure(background='blue')
            logging.debug("changing background color")
            question_response = answer_mode(question_asked)
            text_to_speech(question_response)


def create_thread() -> None:
    """To process multiple threads at same time."""
    try:
        x = threading.Thread(target=controller)
        x.setDaemon(True)
        x.start()
    except Exception:
        logging.error(Exception.message)

# toggle mode for ON/OFF requirement


def Simpletoggle() -> None:
    """
    ON/OFF mode for echo
    with welcome messages.
    """
    global Mode
    if toggle_button.config('text')[-1] == 'ON':
        try:
            Mode = True
            text_to_speech("Welcome this is alexa")
            create_thread()
            toggle_button.config(text='OFF')
        except Exception:
            logging.error("Echo API is unavailable!, check microsoft support!")
            sys.exit()
    else:
        toggle_button.config(text='ON')
        root.update
        logging.debug("Echo Ending..")
        text_to_speech("GoodBye")
        Mode = False

# Main Amazon echo Tkinter GUI configurations


if __name__ == "__main__":
    root = Tk()
    my_gui = root
    my_gui.title("Amazon Echo")
    my_gui.configure(background='grey')
    my_gui.geometry("300x500")
    toggle_button = Button(my_gui,
                           text="ON",
                           command=Simpletoggle,
                           height=2,
                           width=4)
    toggle_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()
