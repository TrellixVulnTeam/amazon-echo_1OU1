from answer_service import answer_mode


def test_answer_mode():
    """
    checking if answer mode returns correct answer
    """
    x = answer_mode("2+2")
    assert x == '4'


def test_answer_mode_():
    """
    checking if answer mode returns correct answer
    """
    x = answer_mode("capital city of UK")
    assert 'on' in x
