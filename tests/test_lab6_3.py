from src.lab6_3 import *

def __helper(y, should_be_leapyear):
    n = "not " if not should_be_leapyear else ""
    assert is_leapyear(y) == should_be_leapyear, f"{y} is {n}a leap year"

def test_2000_is_leap_year():
    __helper(2000, True)

def test_2004_is_leap_year():
    __helper(2004, True)

def test_2312_is_leap_year():
    __helper(2312, True)

def test_1836_is_leap_year():
    __helper(1836, True)

def test_1600_is_leap_year():
    __helper(1600, True)

def test_2400_is_leap_year():
    __helper(2400, True)

def test_2001_is_not_leap_year():
    __helper(2001, False)

def test_1900_is_not_leap_year():
    __helper(1900, False)

def test_2100_is_not_leap_year():
    __helper(2100, False)

def test_float_is_not_leap_year():
    __helper(20.0, False)

def test_a_is_not_leap_year():
    __helper("a", False)