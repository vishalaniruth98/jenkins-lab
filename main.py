"""Python Program to perform various unittesting functions"""
import unittest
from Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    """Calculator"""
    calculator = Calculator()
    def test_add(self):
        """Addition"""
        self.assertEqual(4, self.calculator.add(2, 2))
        self.assertEqual(3.2, self.calculator.add(1, 2.2))

    def test_minus(self):
        """Subtraction"""
        self.assertEqual(2, self.calculator.minus(3, 1))
        self.assertEqual(-2, self.calculator.minus(1, 3))

    def test_multiple(self):
        """Multiply"""
        self.assertEqual(12, self.calculator.multiple(3, 4))
        self.assertEqual(13.5, self.calculator.multiple(3, 4.5))

    def test_devide(self):
        """Divide"""
        self.assertEqual(3, self.calculator.devide(9, 3))

        # How to deal with Exception in TDD?
        #self.assertRaises(ZeroDivisionError, self.calculator.devide(3, 0))

    def test_issame(self):
        """IsTrue"""
        self.assertIs(True, self.calculator.issame(13, 13))
        self.assertIs(False, self.calculator.issame(13, 14))

    def test_is_substring(self):
        """Checks whether is substring or not"""
        self.assertIs(False, self.calculator.isSubstring("hello world", "hello"))
        #self.assertIs(False, self.calculator.isSubstring("return error", "hello"))

    def test_is_greater_lesser(self):
        """>,<,>=,<="""
        self.assertGreater(10, 8)
        self.assertGreaterEqual(10, 8)
        self.assertLess(7, 8)
        self.assertLessEqual(8, 8)

    def test_count_equal(self):
        """Checks whether two lists are equal"""
        var_a = [1, 2, 3, 4]
        var_b = [4, 3, 2, 1]
        self.assertCountEqual(var_a, var_b)

if __name__ == "__main__":
    unittest.main()
