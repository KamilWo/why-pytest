import unittest


# function to test
def add_three(number):
    return number + 3


class AddThreeTests(unittest.TestCase):
    
    def testAddThree(self):
        self.assertEqual(add_three(5), 8)


if __name__ == '__main__':
    unittest.main()


"""
Test run:

python unit_test_1.py

Result:


.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

"""
