import pytest


# function to test
def add_three(number):
    return number + 3

def test_add_three():
    assert add_three(5) == 8


"""
Test run:

py.test 2_pytest_example.py

Result: 
============================= test session starts =============================

[...]

collected 1 items

2_pytest_example.py .

========================== 1 passed in 0.01 seconds ===========================

"""
