import psycopg2

connection = psycopg2.connect(
    dbname='treatment_of_goods',
    user='dbuser',
    password='dbpassword',
    host='localhost'
)

