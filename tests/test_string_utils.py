import pytest
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../sample_ptc')))

from string_utils import StringUtils

def test_to_upper():
    assert StringUtils.to_upper("hello") == "HELLO"
    assert StringUtils.to_upper("HeLLo") == "HELLO"
    assert StringUtils.to_upper("") == ""

def test_to_lower():
    assert StringUtils.to_lower("HELLO") == "hello"
    assert StringUtils.to_lower("HeLLo") == "hello"
    assert StringUtils.to_lower("") == ""

def test_is_palindrome():
    assert StringUtils.is_palindrome("madam") is True
    assert StringUtils.is_palindrome("racecar") is True
    assert StringUtils.is_palindrome("hello") is False
    assert StringUtils.is_palindrome("A man, a plan, a canal: Panama") is True
    assert StringUtils.is_palindrome("") is True

def test_reverse():
    assert StringUtils.reverse("hello") == "olleh"
    assert StringUtils.reverse("a") == "a"
    assert StringUtils.reverse("") == ""

def test_count_vowels():
    assert StringUtils.count_vowels("hello") == 2
    assert StringUtils.count_vowels("HELLO") == 2
    assert StringUtils.count_vowels("rhythm") == 0
    assert StringUtils.count_vowels("") == 0

def test_epoch_seconds_as_string():
    dt = datetime(2024, 1, 1, 0, 0, 0)
    assert StringUtils.epoch_seconds_as_string(dt) == str(int(dt.timestamp()))

def test_epoch_millis_as_string():
    dt = datetime(2024, 1, 1, 0, 0, 0)
    assert StringUtils.epoch_millis_as_string(dt) == str(int(dt.timestamp() * 1000))

def test_human_readable_datetime():
    dt = datetime(2024, 1, 1, 12, 34, 56)
    assert StringUtils.human_readable_datetime(dt) == "2024-01-01 12:34:56"