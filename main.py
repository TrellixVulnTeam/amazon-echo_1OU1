from tkinter import CENTER, Tk, Button
from listening_service import record, speech_to_text
from database_retriv import retrieve_file
from txt_to_speech import text_to_speech
from answer_service import answer_mode
import threading
import sys

# beginning and middleware for echo application


def controller():
    """
    this function acts as a directional service
    for play and questions
    """
    while True:
        my_gui.configure(background='cyan')
        print("listening...")
        record()
        x = speech_to_text()
        if "play" in x:
            requested = x.replace('play', '').replace('.', '').lower().strip()
            my_gui.configure(background='green')
            try:
                retrieve_file(requested)
            except Exception:
                controller()
        else:
            question_asked = x
            my_gui.configure(background='blue')
            try:
                question_response = answer_mode(question_asked)
                text_to_speech(question_response)
            except Exception:
                controller()


def create_thread():
    """
    threading to solve frozen ON button.
    """
    try:
        threading.Thread(target=controller).start()
    except Exception:
        print(Exception.message)

# toggle mode for ON/OFF requirement


def Simpletoggle():
    """
    ON/OFF mode for echo
    with welcome messages.
    """
    if toggle_button.config('text')[-1] == 'ON':
        try:
            text_to_speech("Welcome this is alexa")
            create_thread()
            toggle_button.config(text='OFF')
        except Exception:
            Simpletoggle()
    else:
        toggle_button.config(text='ON')
        text_to_speech("GoodBye")
        sys.exit()

# Main Amazon echo Tkinter GUI configurations


root = Tk()
my_gui = root
my_gui.title("Amazon Alexa")
my_gui.configure(background='grey')
my_gui.geometry("300x500")
toggle_button = Button(my_gui,
                       text="ON",
                       command=Simpletoggle,
                       height=2,
                       width=4)
toggle_button.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
