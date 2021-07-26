"""
Основной файл программы.
Берет данные из модуля work_with_json и производит создание таблиц, добавление и изменение данных в них.
"""


import sqlite3
import sys
from work_with_json import load_data_from_json, validate_json


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
                id integer PRIMARY KEY AUTOINCREMENT,
                name varchar(255) NOT NULL,
                package_height float NOT NULL,
                package_width float NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS shops_goods (
                id integer PRIMARY KEY AUTOINCREMENT,
                good_id integer NOT NULL,
                location varchar(255) NOT NULL,
                amount integer NOT NULL,
                FOREIGN KEY (good_id)  REFERENCES goods (id)
        )
        """
    )
    connection.commit()


def fill_db(file: dict) -> None:
    """Функция, осуществляющая добавление или изменение данных в БД."""
    global cursor
    global connection
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
    cursor.execute(f"""SELECT * FROM goods WHERE id={id}""")
    check = cursor.fetchone()
    if check != None:
        cursor.execute(
            f"""
            UPDATE goods SET name='{name}', package_height='{height}', package_width='{width}' 
            WHERE id={id}
            """
        )
        for element in range(len(location)):
            cursor.execute(
                f"""
                UPDATE shops_goods SET amount='{amount[element]}' 
                WHERE good_id={id} AND location='{location[element]}'
                """
            )
        connection.commit()
        print("Данные изменены.")
    else:
        cursor.execute(
            f"""
            INSERT INTO goods (id, name, package_height,package_width) 
            VALUES ({id}, '{name}', '{height}', '{width}')
            """
        )
        for element in range(len(location)):
            cursor.execute(
                f"""
                INSERT INTO shops_goods (good_id, location, amount) 
                VALUES ({id}, '{location[element]}', '{amount[element]}')
                """
            )
        connection.commit()
        print("Данные добавлены.")


if __name__ == "__main__":
    create_db()
    data = load_data_from_json(path_to_json)
    if validate_json(data):
        print("Загрузка прошла успешно, база данных обновлена.")
        fill_db(data)
        for row in cursor.execute("""SELECT * FROM goods"""):
            print(row)
        for row in cursor.execute("""SELECT * FROM shops_goods"""):
            print(row)
    connection.close()
