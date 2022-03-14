"""
Text to Speech
========================
Text to speech method
-------------------------
Text to speech converter
...........................

*Use it like this*::

    from txt_to_speech import text_to_speech

    text_to_speech("what is your name")

"""

import requests
from play_service import play
import logging

logging.basicConfig(level=logging.DEBUG)


def text_to_speech(text: str) -> str:
    """function converts text to speech
    uses the request module to send
    text content to microsoft returns
    binary data.

    Args:
        text (str):  A string of text.

    Returns:
        str: returns text in the form of binary
    """
    url = 'https://uksouth.tts.speech.microsoft.com/cognitiveservices/v1'
    headers = {'Ocp-Apim-Subscription-Key': '0f70d918db4c44a5a4de61226a84c114',
               'Content-Type': 'application/ssml+xml',
               'X-Microsoft-OutputFormat': 'riff-16khz-16bit-mono-pcm'
               }
    voice = "en-US-EricNeural"
    to_text = text
    data = f"""
    <speak version='1.0' xml:lang='en-US'>
    <voice xml:lang='en-US' xml:gender='Male' name='{voice}'>{to_text}</voice>
    </speak>"""
    try:
        response = requests.post(url, data=data, headers=headers)
        logging.debug(response)
        return play(response.content)
    except Exception:
        logging.error(Exception)
