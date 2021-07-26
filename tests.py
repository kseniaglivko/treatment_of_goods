from work_with_json import load_data_from_json, validate_json
import unittest


class TestJsonToDbMethods(unittest.TestCase):

    def test_empty_field(self):
        self.assertRaises(Exception, load_data_from_json, "./test_files/test_no_name.json")

    def test_no_field(self):
        self.assertRaises(Exception, validate_json, "./test_files/test_no_id.json")

    def test_wrong_format(self):
        self.assertRaises(Exception, load_data_from_json, "./test_files/test_wrong_format.json")


if __name__ == "__main__":
    unittest.main()