import sqlite3
import sys
import work_with_json

"""Передаем введенный через консоль путь до файла в переменную"""
path_to_json = str(sys.argv[1])


connection = sqlite3.connect("treatment_of_goods.db")

cursor = connection.cursor()


def create_db() -> None:
    """Содание базы данных, а именно: две основные таблицы 'goods' и 'shops_goods'"""
    global cursor

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS goods (
                id integer NOT NULL,
                name varchar(255) NOT NULL,
                package_height float NOT NULL,
                package_width float NOT NULL
        );
        """)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS shops_goods (
                id integer NOT NULL,
                good_id integer REFERENCES goods (id) NOT NULL,
                location varchar(255) NOT NULL,
                amount integer NOT NULL
        );
        """)

    connection.commit()


def fill_db(file: dict) -> None:
    """Фнукция, осуществляющая загрузку данных в базу данных."""
    global cursor
    for key, value in file.items():
        if key == "id":
            id = value
        if key == "name":
            name = value
        if key == "package_params":
            width = value["width"]
            height = value["height"]
        if key == "location_and_quantity":
            location = list()
            amount = list()
            for element in value:
                location.append(element["location"])
                amount.append(element["amount"])

