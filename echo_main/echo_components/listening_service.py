"""
Listening service
=========================================
Records users voice into text
------------------------------------------
Listens users voice into text
..........................................

*Use it like this*::
    record() #  this will start voice recording
"""


import pyaudio
import wave
import logging


logger = logging.getLogger(__name__)


def record(duration=5.0) -> bool:
    """pyaudio records users voice and converts
    to wav format

    Args:
        duration (float, optional): Defaults to 5.0.

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
        print(error)
