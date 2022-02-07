from txt_to_speech import text_to_speech
from unittest import mock


# Mocking the play function being called

def test_text_to_speech():
    with mock.patch('txt_to_speech.play', return_value='Hello'):
        assert text_to_speech("Hello") == "Hello"


def test_text_to_speech_1():
    with mock.patch('txt_to_speech.play', return_value='test'):
        assert text_to_speech("test") == "test"
