import unittest
import my_code

class TestStringMethods(unittest.TestCase):

    def test_01(self):
        self.assertAlmostEqual(my_code.problem01(),2)

if __name__ == '__main__':
    unittest.main()