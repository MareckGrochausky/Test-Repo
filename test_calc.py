import unittest
from calc import Calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc1 = Calculator(1, 2)

        self.assertEqual(calc1.adding(), 3)


if __name__ == "__main__":
    unittest.main()

