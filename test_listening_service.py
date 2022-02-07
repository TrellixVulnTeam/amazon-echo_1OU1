import pytest
import requests


# This module contains unit testing for the listening service folder
# MOCK TESTING FOR FUNCTION MAKING A RESPONSE.


def test_speech_to_text():
    with open("dd.wav", 'rb') as file:
        binary = file.read()
        url = ('https://uksouth.stt.speech.microsoft.com/speech/'
               'recognition/conversation/cognitiveservices/v1')
        params = {"language": "en-GB"}
        headers = {
         "Content-Type": "audio/wav",
         "Accept": "application/json",
         "Ocp-Apim-Subscription-Key": "aec62efd1ccd427f886ca2ca1a1a47a6"
        }
        try:
            response = requests.post(url,
                                     params=params,
                                     headers=headers,
                                     data=binary)
            response = response.json()
            return response
        except Exception:
            print(Exception.message)
    assert response.status_code == 200


def test_text2speech_errorHandle():
    with pytest.raises(Exception):
        with open("dd.wav", 'rb') as file:
            binary = file.read()
        params = {"language": "en-GB"}
        url = ""
        headers = {
         "Content-Type": "audio/wav",
         "Accept": "application/json",
         "Ocp-Apim-Subscription-Key": "aec62efd1ccd427f886ca2ca1a1a47a6"
        }
        try:
            response = requests.post(url,
                                     params=params,
                                     headers=headers,
                                     data=binary)
            response = response.json()
            return response
        except Exception:
            print(Exception.message)
