import unittest
from calc import Calculator


class TestCalculator(unittest.TestCase):
    def test_multip(self):
        calc1 = Calculator(1, 2)

        self.assertEqual(calc1.multip(), 2)

    def test_multip2(self):
        calc1 = Calculator(1, 2)

        self.assertEqual(calc1.multip(), 2)


if __name__ == "__main__":
    unittest.main()
