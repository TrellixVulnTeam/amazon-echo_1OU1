"""
Speech to text
=================================================
Converts speech to text
-------------------------------------------------
.................................................

*Use it like this*::

    from speech_to_txt import speech_to_text
    speech_to_text()

"""

import requests


def speech_to_text() -> None:
    """ reads the dd.wav and sends the data to
    microsoft api to translate into english text

    Returns: text form of speech is returned
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
        response = response.json()
        return response["DisplayText"].lower()
    except Exception:
        print("Error converting speech to text")
