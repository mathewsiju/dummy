""" Test fail
"""
import unittest
class TestExample(unittest.TestCase):
    """
        sample description   
    """
    def test_always_true(self):
        self.assertEqual(333, 1)

if __name__ == '__main__':
    unittest.main()


