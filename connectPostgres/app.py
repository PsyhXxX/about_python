import psycopg2

DATABASE_NAME = "my_database"
DATABASE_HOST = "192.168.0.30"
USER_DATABASE = "mydabuser"
USER_DATABASE_PASSWORD = "12345678"
DATABASE_PORT = "5432"

conn = psycopg2.connect(dbname=DATABASE_NAME, host=DATABASE_HOST, user=USER_DATABASE, password=USER_DATABASE_PASSWORD, port=DATABASE_PORT)
print("Подключение к БД установлено")
print(conn.get_dsn_parameters())

conn.autocommit = True  # устанавливаем актокоммит
cursor = conn.cursor()

cursor.execute("SELECT * FROM mydabuser.person")

cursor.close()
conn.close()
