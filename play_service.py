import pyaudio
import wave
import io
import logging

logger = logging.getLogger(__name__)
CHUNK = 1024


def play(audio_in: any):
    logger.debug("playing %s", str(audio_in))
    p = pyaudio.PyAudio()
    if isinstance(audio_in, type(b'')):
        wf = wave.open(io.BytesIO(audio_in), 'rb')
    else:
        try:
            wf = wave.open(audio_in, 'rb')
        except FileNotFoundError:
            logger.warning("No such file: %s", audio_in)
            raise FileNotFoundError
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(), rate=wf.getframerate(),
                    output=True)
    # read data
    data = wf.readframes(CHUNK)
    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()
