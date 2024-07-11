import sqlite3
from werkzeug.security import generate_password_hash

# Conexión a la base de datos
conn = sqlite3.connect('instance/risky_burger.sqlite')
cursor = conn.cursor()

# Crear tabla de administradores
cursor.execute('''
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Crear tabla de elementos del menú
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    ingredients TEXT,
    image TEXT,
    category TEXT NOT NULL
)
''')

# Agregar un administrador por defecto
username = 'admin'
password = generate_password_hash('admin')

cursor.execute('INSERT OR IGNORE INTO admins (username, password) VALUES (?, ?)', (username, password))

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
