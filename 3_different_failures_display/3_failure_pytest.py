import pytest


# function to test
def add_three(number):
    return number + 3

def test_add_three():
    assert add_three(5) == 10


"""
Test run:

py.test 3_failure_pytest.py

Result: (when failure occurs)

============================= test session starts =============================

[...]

collected 1 items

3_failure_pytest.py F

================================== FAILURES ===================================
_______________________________ test_add_three ________________________________

    def test_add_three():
>       assert add_three(5) == 10
E       assert 8 == 10
E        +  where 8 = add_three(5)

3_failure_pytest.py:9: AssertionError
========================== 1 failed in 0.03 seconds ===========================

"""
