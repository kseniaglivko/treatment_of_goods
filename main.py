import sqlite3

connection = sqlite3.connect("treatment_of_goods.db")


def create_db() -> None:
    """Содание базы данных, а именно: две основные таблицы 'goods' и 'shops_goods'"""
    cursor = connection.cursor()

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


