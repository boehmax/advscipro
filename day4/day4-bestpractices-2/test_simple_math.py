# test_simple_math.py
import pytest
# Import the functions to be tested
from simple_math import simple_add, simple_sub, simple_mult, simple_div, poly_first, poly_second

#Test functions


# Test cases for simple_add function
def test_simple_add_positive_numbers():
    assert simple_add(2, 3) == 5

def test_simple_add_negative_numbers():
    assert simple_add(-2, -3) == -5

def test_simple_add_mixed_numbers():
    assert simple_add(2, -3) == -1

# Test cases for simple_sub function
def test_simple_sub_positive_numbers():
    assert simple_sub(5, 3) == 2

def test_simple_sub_negative_numbers():
    assert simple_sub(-2, -3) == 1

def test_simple_sub_mixed_numbers():
    assert simple_sub(2, -3) == 5

# Test cases for simple_mult function
def test_simple_mult_positive_numbers():
    assert simple_mult(2, 3) == 6

def test_simple_mult_negative_numbers():
    assert simple_mult(-2, -3) == 6

def test_simple_mult_mixed_numbers():
    assert simple_mult(2, -3) == -6

# Test cases for simple_div function
def test_simple_div_integer_result():
    assert simple_div(6, 3) == 2

def test_simple_div_float_result():
    assert simple_div(7, 2) == 3.5

def test_simple_div_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        simple_div(5, 0)

# Test cases for poly_first function
def test_poly_first():
    assert poly_first(2, 1, 2) == 5

# Test cases for poly_second function
def test_poly_second():
    assert poly_second(2, 1, 2, 3) == 17
