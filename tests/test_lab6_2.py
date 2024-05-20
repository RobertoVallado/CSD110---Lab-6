import pytest

from src.lab6_2 import *

def test_non_numeric_a():
    try:
        hypotenuse("a", 1)
    except AssertionError as e:
        pass
    except:
        assert False, "The hypotenuse function must raise an AssertionError if the first argument is non-numeric"

def test_non_numeric_a_message():
    with pytest.raises(AssertionError) as err:
        hypotenuse("a", 1)

    assert "Both a and b must be numeric" == str(err.value), "The raised error must have the message 'Both a and b must be numeric' when the first argument is non-numeric"

def test_non_numeric_a():
    try:
        hypotenuse(1, "b")
    except AssertionError as e:
        pass
    except:
        assert False, "The hypotenuse function must raise an AssertionError if the second argument is non-numeric"

def test_non_numeric_a_message():
    with pytest.raises(AssertionError) as err:
        hypotenuse(1, "b")

    assert "Both a and b must be numeric" == str(err.value), "The raised error must have the message 'Both a and b must be numeric' when the second argument is non-numeric"

def test_negative_a_message():
    with pytest.raises(AssertionError) as err:
        hypotenuse(-1, 1)

    assert "Both a and b must be greater than or equal to 0" == str(err.value), "The raised error must have the message 'Both a and b must be greater than or equal to 0' when the first argument is negative"

def test_negative_b_message():
    with pytest.raises(AssertionError) as err:
        hypotenuse(1, -1)

    assert "Both a and b must be greater than or equal to 0" == str(err.value), "The raised error must have the message 'Both a and b must be greater than or equal to 0' when the second argument is negative"

def test_a_0():
    assert hypotenuse(0, 10) == 10, "The hypotenuse must be equal to the second argument when the first argument is 0"

def test_b_0():
    assert hypotenuse(10, 0) == 10, "The hypotenuse must be equal to the first argument when the second argument is 0"

def test_3_4_5():
    assert hypotenuse(3,4) == 5.0, "The hypotenuse must equal 5 for a=3 and b=4"

def test_1_1_sqrt2():
    assert hypotenuse(1,1) == math.sqrt(2), "The hypotenuse must equal sqrt(2) for a=1 and b=1"
