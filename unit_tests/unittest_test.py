from math_utils import *
from math_utils.decorators import math_decorators
import unittest


class TestMyFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-3, 5), -8)
        self.assertEqual(subtract(0, 1), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)

    def test_zero_divide(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_only_int_float_incorrect(self):
        params = [
            (0, "a"),
            ("a", "a"),
        ]
        for a, b in params:
            with self.subTest(a=a, b=b):
                @math_decorators.only_int_float_func
                def mock(a, b):
                    pass

                with self.assertRaises(TypeError):
                    mock(a, b)

    def test_only_int_float_correct(self):
        params = [
            (0, 0),
            (0, 0.1),
            (0.1, 0.1)
        ]
        for a, b in params:
            with self.subTest(a=a, b=b):
                @math_decorators.only_int_float_func
                def mock(a, b):
                    pass
                
                mock(a, b)
