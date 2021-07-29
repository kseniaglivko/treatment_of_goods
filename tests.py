from work_with_json import load_data_from_json, validate_json
import unittest


class TestTreatmentOfGoods(unittest.TestCase):

    def test_empty_field(self):
        self.assertRaises(Exception, load_data_from_json, "./test_files/test_no_name.json")

    def test_no_field(self):
        self.assertRaises(Exception, validate_json, "./test_files/test_no_id.json")

    def test_wrong_format(self):
        self.assertRaises(Exception, load_data_from_json, "./test_files/test_wrong_format.json")

    def test_ok(self):
        self.assertEqual(load_data_from_json("./test_files/test_ok.json"),
        {'id': 12, 'name': 'Телевизор', 'package_params': {'width': 100, 'height': 50},
         'location_and_quantity': [{'location': 'Магазин на Пушкина', 'amount': 100},
                                   {'location': 'Магазин на Колотушкина', 'amount': 50}]})


if __name__ == "__main__":
    unittest.main()
