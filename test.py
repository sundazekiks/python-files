import pytest
from passwords import word_complexity, check_complexity, word_in_file, password_strength

def test_word_complexity():
    assert word_in_file("daniel", "C:\\Users\\Danny\\Documents\\cse111\\w02\\lists\\wordlist.txt", "C:\\Users\\Danny\\Documents\\cse111\\w02\\lists\\toppasswords.txt") == False