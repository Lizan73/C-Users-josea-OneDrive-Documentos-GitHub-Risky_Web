import sqlite3

# Conectar a la base de datos
connection = sqlite3.connect('instance/risky_burger.sqlite')

with connection:
    # Verificar la existencia de las tablas
    tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print("Tables in the database:", tables)

    # Verificar los registros en la tabla de administradores
    admins = connection.execute("SELECT * FROM admins;").fetchall()
    print("Admins:", admins)

connection.close()
