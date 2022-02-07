import pytest


# Mocking listening controller

@pytest.mark.parametrize("data", [("play song 1"),
                                  ("play noise 2"),
                                  ("play sounds")])
def test_controller(data):
    if "play" in data:
        x = "play"
    else:
        x = "answer"
        assert x == "play"


@pytest.mark.parametrize("answer_mock", [("what is the capaital city of uk"),
                                         ("who is the inventor of python"),
                                         ("what is the weather like in Uk")])
def test_controlle_1(answer_mock):
    if "play" in answer_mock:
        x = "play"
    else:
        x = "answer"
        assert x == "answer"
