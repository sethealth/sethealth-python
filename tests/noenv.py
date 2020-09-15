import unittest
import sethealth


class TestAPI(unittest.TestCase):
    def test_missing_environment_variables(self):
        with self.assertRaises(sethealth.InputException):
            sethealth.Client()


if __name__ == "__main__":
    unittest.main()
