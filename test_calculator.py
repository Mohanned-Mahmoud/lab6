import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Test cases for the add function
        self.assertEqual(add(60, 4), 64)
        self.assertEqual(add(-40, 4), -36)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

if __name__ == "__main__":
    unittest.main()
