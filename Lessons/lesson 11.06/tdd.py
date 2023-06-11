import unittest

def multiply(a, b):
    res = 0
    if b < 0:
        a, b = -a, -b
    for i in range(b):
        res += a
    return res    

class MultTestCase(unittest.TestCase):

    def test_base_scenario(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_left_zero_case(self):
        result = multiply(0, 3)
        self.assertEqual(result, 0)

    def test_right_zero_case(self):
        result = multiply(2, 0)
        self.assertEqual(result, 0)

    def test_left_one_case(self):
        result = multiply(1, 3)
        self.assertEqual(result, 3)

    def test_right_one_case(self):
        result = multiply(2, 1)
        self.assertEqual(result, 2)

    def test_left_negative_case(self):
        result = multiply(-2, 3)
        self.assertEqual(result, -6)

    def test_right_negative_case(self):
        result = multiply(2, -3)
        self.assertEqual(result, -6)

    def test_base_negative_scenario(self):
        result = multiply(-2, -3)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
