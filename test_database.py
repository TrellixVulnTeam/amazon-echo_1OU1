import pytest
from database_entry import insert_file, convert_into_binary


def test_insert_file():
    with pytest.raises(Exception):
        assert insert_file("dd.wav", "sample.db", "audio", "music", "loud")


def test_convert_into_binary():
    assert convert_into_binary("dd.wav") is not None

# check if binary value


def test_convert_into_binary_new():
    assert 1 in convert_into_binary("dd.wav")
