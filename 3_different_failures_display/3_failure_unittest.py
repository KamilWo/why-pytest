import unittest


# function to test
def add_three(number):
    return number + 3


class AddThreeTests(unittest.TestCase):
    
    def testAddThree(self):
        self.assertEqual(add_three(5), 10)


if __name__ == '__main__':
    unittest.main()


"""
Test run:

python 3_failure_unittest.py

Result: (when failure occurs)

F
======================================================================
FAIL: testAddThree (__main__.AddThreeTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "3_failure_unittest.py", line 12, in testAddThree
    self.assertEqual(add_three(5), 10)
AssertionError: 8 != 10

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

"""
