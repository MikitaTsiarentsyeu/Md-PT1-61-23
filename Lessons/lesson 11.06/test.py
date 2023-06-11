import unittest
from unittest.mock import MagicMock

class Calculator:

    def add(self, a, b):
        return a+b
    
class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()
    
    # def tearDown(self) -> None:
    #     return super().tearDown()

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_negative_add(self):
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)

def get_data(api):
    response = api.get("/data/")
    if response:
        data = response.json()
        return data["data"]
    
class ApiTestCase(unittest.TestCase):

    def test_api(self):
        mock_api = MagicMock()
        mock_api.get.return_value.json.return_value = {"data": [1,2,3]}

        result = get_data(mock_api)
        self.assertEqual(result, (1,2,3))


if __name__ == "__main__":
    unittest.main()