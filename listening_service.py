import pyaudio
import wave
import logging
import requests


logger = logging.getLogger(__name__)


def record(duration=5.0) -> bool:
    """
    pyaudio records users voice and converts
    to wav format
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


def speech_to_text():
    """
    reads the dd.wav and sends the data to
    microsoft api to translate into english text
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
         "Ocp-Apim-Subscription-Key": "aec62efd1ccd427f886ca2ca1a1a47a6"}
        response = requests.post(url,
                                 params=params,
                                 headers=headers,
                                 data=binary)
        response = response.json()
        return response["DisplayText"].lower()
    except Exception:
        print("Error converting speech to text")
