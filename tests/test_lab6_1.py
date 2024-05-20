import sys
import tests.util as util

from src.lab6_1 import *

def test_non_numeric():
    assert not is_numeric("A"), "is_numeric must return False for non-numeric arguments"

def test_int():
    assert is_numeric(1), "is_numeric must return True for integer arguments"

def test_negative():
    assert is_numeric(-1), "is_numeric must return True for negative arguments"

def test_float():
    assert is_numeric(3.14159), "is_numeric must return True for floating point arguments"