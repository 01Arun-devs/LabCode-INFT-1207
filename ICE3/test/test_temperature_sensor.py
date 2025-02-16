import unittest
from ICE3.src.temperature_sensor import temp_sensor

class TestTemperatureSensor(unittest.TestCase):

    # Boundary Value Analysis (BVA)
    def test_case_1_min_boundary(self):
        input_temps = [-50]
        expected = {"Min": "-50°C", "Max": "-50°C", "Avg": "-50.00°C"}
        result = temp_sensor(input_temps)
        self.assertEqual(result, expected)

    def test_case_2_max_boundary(self):
        input_temps = [150]
        expected = {"Min": "150°C", "Max": "150°C", "Avg": "150.00°C"}
        result = temp_sensor(input_temps)
        self.assertEqual(result, expected)

    def test_case_3_near_boundary(self):
        input_temps = [-49, 149]
        expected = {"Min": "-49°C", "Max": "149°C", "Avg": "50.00°C"}
        result = temp_sensor(input_temps)
        self.assertEqual(result, expected)

    # Robustness Testing
    def test_case_4_mixed_valid_invalid(self):
        input_temps = [-60, 20, 160]
        result = temp_sensor(input_temps)
        self.assertEqual(result, "Out-of-bound value detected.")

    def test_case_5_alphabetic_input(self):
        input_temps = [20, "abc", 30]
        result = temp_sensor(input_temps)
        self.assertEqual(result, "Invalid input detected.")

    def test_case_6_special_characters_input(self):
        input_temps = [10, "@", -40]
        result = temp_sensor(input_temps)
        self.assertEqual(result, "Invalid input detected.")

    # Special Scenarios
    def test_case_7_extreme_values(self):
        input_temps = [2 ** 31 - 1, -2 ** 31]
        result = temp_sensor(input_temps)
        self.assertEqual(result, "Out-of-bound value detected.")

    def test_case_8_all_same_values(self):
        input_temps = [50, 50, 50]
        expected = {"Min": "50°C", "Max": "50°C", "Avg": "50.00°C"}
        result = temp_sensor(input_temps)
        self.assertEqual(result, expected)

    def test_case_9_empty_list(self):
        input_temps = []
        result = temp_sensor(input_temps)
        self.assertEqual(result, "No input provided.")


if __name__ == '__main__':
    unittest.main()