import requests
from play_service import play


def text_to_speech(text: str) -> str:
    url = 'https://uksouth.tts.speech.microsoft.com/cognitiveservices/v1'
    headers = {'Ocp-Apim-Subscription-Key': 'aec62efd1ccd427f886ca2ca1a1a47a6',
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
        return play(response.content)
    except Exception:
        print(Exception.message)
