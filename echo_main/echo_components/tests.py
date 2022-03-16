from answer_service import answer_mode
import pytest
from database_entry import convert_into_binary, sqlite_connect, insert_file
from unittest import mock
from txt_to_speech import text_to_speech
# from listening_service import speech_to_text, record
from database_retriv import retrieve_file
# from main import controller
import requests
from speech_to_txt import speech_to_text


def test_answer_mode():
    """
    checking if answer mode returns correct answer
    """
    x = answer_mode("2+2")
    assert x == '4'


def test_answer_mode_1():
    """
    checking if answer mode returns correct answer
    """
    x = answer_mode("capital city of UK")
    assert 'on' in x


# @mock.patch('answer_service.requests.get')
# def test_answer_mode3(mocked_post: Mock):
#     """
#     checking if data can be read by selected filters
#     """
#     response_mock = Mock(status_code=200)
#     response_mock.json.return_value = {'queryresult': "data"}
#     mocked_post.return_value = response_mock
#     assert "Boris" in answer_mode("test")


@mock.patch('requests.get', return_value="")
def test_answer_mode_4(mocked_post):
    """
    forcing an exception, test to see if raised.
    """
    with pytest.raises(Exception):
        assert answer_mode("") == "test"


# def test_answer_service():
#     """
#     test to see if module can be imported.
#     """
#     import answer_service
#     assert answer_service == True


def test_convert_into_binary():
    """
    test to check if exception raises for wrong file.
    """
    with pytest.raises(Exception):
        assert convert_into_binary('dummyfile')


def test_convert_into_binary1():
    assert convert_into_binary("dd.wav") is not None

# this may fail at first


def test_convert_into_binary2():
    """ test to see if audio is in binary after convert
    """
    assert 1 in convert_into_binary("dd.wav")


@mock.patch('database_entry.sqlite3.connect', return_value='True')
def tests_sqlite_connect(test):
    """
    test to check if database can be connnected to
    """
    assert sqlite_connect("test") == "True"


@mock.patch('txt_to_speech.play', return_value='True')
def tests_text_to_speech1(req_test):
    assert text_to_speech("test") == 'True'


@mock.patch('txt_to_speech.requests', return_value='')
def tests_text_to_speech2(req_test):
    """
    forcing an exception test
    """
    with pytest.raises(Exception):
        assert text_to_speech("test")


@mock.patch("requests.post")
@mock.patch("txt_to_speech.play", return_value="test")
def test_myfunction_3(mocked_post, mok_re):
    """
    test to check if function is returned
    """
    mocked_post.return_value = "Findme"
    assert text_to_speech("mock") == "Findme"


def test_insert_file():
    """ testing for exception
    """
    with pytest.raises(Exception):
        assert insert_file("dd.wav", " ", "audio", "music", "loud")


@pytest.mark.parametrize("data", [("play song 1"),
                                  ("play noise 2"),
                                  ("play sounds")])
def test_controller(data):
    """mocking controller and condition.
    """
    if "play" in data:
        x = "play"
    else:
        x = "answer"
        assert x == "play"


# Mocking listening controller

@pytest.mark.parametrize("answer_mock", [("what is the capaital city of uk"),
                                         ("who is the inventor of python"),
                                         ("what is the weather like in Uk")])
def test_controlle_1(answer_mock):
    """
    mocking controller and condition.
    """
    if "play" in answer_mock:
        x = "play"
    else:
        x = "answer"
        assert x == "answer"


@mock.patch('requests.post')
def test_answer_modeP(post_mock):
    """
    exception testing
    """
    post_mock.side_effect = requests.exceptions.ConnectionError()
    with pytest.raises(Exception):
        assert answer_mode(22)


def test_retrieve_file():
    """ exception test for db retrival
    """
    with mock.patch("database_retriv.sqlite_connect") as mockdb:
        mockdb.add = mock.MagicMock(return_value="True")
        with pytest.raises(Exception):
            assert retrieve_file("dd.wav") == 'd'


@mock.patch("speech_to_txt.requests.post")
def test_speech_to_text(mocked_post):
    mocked_post.return_value.json.return_value = {"DisplayText": "test"}
    assert speech_to_text() == "test"


# attempting test on listening service

# @mock.patch("listening_service.record")
# def test_listening_service(mocked_listen: MagicMock):
#    record()
#    mocked_listen.assert_called_once()
