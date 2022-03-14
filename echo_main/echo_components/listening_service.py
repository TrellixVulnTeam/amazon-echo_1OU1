"""
Listening service
=========================================
Listens & Translate users voice into text
------------------------------------------
Listens & Translate users voice into text
..........................................

*Use it like this*::
    record() #  this will start voice recording
    speech_to_text() # convert stored audio to text
"""


import pyaudio
import wave
import logging
import requests


logger = logging.getLogger(__name__)


def record(duration=5.0) -> bool:
    """pyaudio records users voice and converts
    to wav format

    Args:
        duration (float, optional): _description_. Defaults to 5.0.

    Returns:
        bool: Microphone begins recording voice
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)
    logger.info("recording for %s seconds", duration)
    frames = []
    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
    logger.info("done recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    try:
        wf = wave.open('dd.wav', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    except Exception as error:
        print("Error:" + error.message)


def speech_to_text() -> None:
    """ reads the dd.wav and sends the data to
    microsoft api to translate into english text

    Returns:
        _type_: text form of speech is returned
    """
    try:
        with open("dd.wav", 'rb') as file:
            binary = file.read()
        url = ('https://uksouth.stt.speech.microsoft.com/'
               'speech/recognition/conversation/cognitiveservices/v1')
        params = {"language": "en-GB"}
        headers = {
         "Content-Type": "audio/wav",
         "Accept": "application/json",
         "Ocp-Apim-Subscription-Key": "0f70d918db4c44a5a4de61226a84c114"}
        response = requests.post(url,
                                 params=params,
                                 headers=headers,
                                 data=binary)
        print(response.content)
        response = response.json()
        return response["DisplayText"].lower()
    except Exception:
        print("Error converting speech to text")
