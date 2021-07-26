"""

Модуль, в котором содержатся функции, предназначенные для обработки json-файл и передачи извлеченных данных в базу.

"""


import jsonschema
import json


def validate_json(file: dict) -> bool:
    """Валидация json-файла."""
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": "http://example.com/example.json",
        "type": "object",
        "title": "The root schema",
        "description": "The root schema comprises the entire JSON document.",
        "default": {},
        "examples": [
            {
                "id": 123,
                "name": "Телевизор",
                "package_params": {"width": 5, "height": 10},
                "location_and_quantity": [
                    {"location": "Магазин на Ленина", "amount": 7},
                    {"location": "Магазин в центре", "amount": 3},
                ],
            }
        ],
        "required": ["id", "name", "package_params", "location_and_quantity"],
        "properties": {
            "id": {
                "$id": "#/properties/id",
                "type": "integer",
                "title": "The id schema",
                "description": "An explanation about the purpose of this instance.",
                "default": 0,
                "examples": [123],
            },
            "name": {
                "$id": "#/properties/name",
                "type": "string",
                "title": "The name schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": ["Телевизор"],
            },
            "package_params": {
                "$id": "#/properties/package_params",
                "type": "object",
                "title": "The package_params schema",
                "description": "An explanation about the purpose of this instance.",
                "default": {},
                "examples": [{"width": 5, "height": 10}],
                "required": ["width", "height"],
                "properties": {
                    "width": {
                        "$id": "#/properties/package_params/properties/width",
                        "type": "integer",
                        "title": "The width schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [5],
                    },
                    "height": {
                        "$id": "#/properties/package_params/properties/height",
                        "type": "integer",
                        "title": "The height schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [10],
                    },
                },
            },
            "location_and_quantity": {
                "$id": "#/properties/location_and_quantity",
                "type": "array",
                "title": "The location_and_quantity schema",
                "description": "An explanation about the purpose of this instance.",
                "default": [],
                "examples": [
                    [
                        {"location": "Магазин на Ленина", "amount": 7},
                        {"location": "Магазин в центре", "amount": 3},
                    ]
                ],
                "items": {
                    "anyOf": [
                        {
                            "$id": "#/properties/location_and_quantity/items/anyOf/0",
                            "type": "object",
                            "title": "The first anyOf schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {"location": "Магазин на Ленина", "amount": 7}
                            ],
                            "required": ["location", "amount"],
                            "properties": {
                                "location": {
                                    "$id": "#/properties/location_and_quantity/items/anyOf/0/properties/location",
                                    "type": "string",
                                    "title": "The location schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": ["Магазин на Ленина"],
                                },
                                "amount": {
                                    "$id": "#/properties/location_and_quantity/items/anyOf/0/properties/amount",
                                    "type": "integer",
                                    "title": "The amount schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": 0,
                                    "examples": [7],
                                },
                            },
                        }
                    ],
                    "$id": "#/properties/location_and_quantity/items",
                },
            },
        },
    }
    try:
        jsonschema.validate(file, schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


def load_data_from_json(path_to_file: str) -> dict:
    """Функция, осуществляющая чтение из файла и загрузку данных из файла в словарь."""
    with open(path_to_file, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.decoder.JSONDecodeError:
            print("Проверьте форматирование JSON-файла, обнаружены ошибки.")
