import sqlite3
from werkzeug.security import generate_password_hash

# Conexión a la base de datos
conn = sqlite3.connect('instance/risky_burger.sqlite')
cursor = conn.cursor()

# Eliminar tablas existentes
cursor.execute('DROP TABLE IF EXISTS admins')
cursor.execute('DROP TABLE IF EXISTS menu_items')

conn.execute('''
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    ingredients TEXT,
    image TEXT,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Agregar un administrador por defecto
conn.execute('INSERT INTO admins (username, password) VALUES (?, ?)',
             ('admin', generate_password_hash('password')))


# Agregar un producto de cada categoría
menu_items = [
    {
        "name": "Fake Hot Dog",
        "description": "Una patty de 100 gr en forma de perrito rellena de queso emmental, papas de bacon crunch, cebolla crunch, queso cheddar y salsa secret-mayo",
        "ingredients": "Patty de carne, queso emmental, bacon, cebolla, queso cheddar, salsa",
        "image": "/static/images/fake_hot_dog.png",
        "category": "Brioche's",
        "price": 6.50
    },
    {
        "name": "Miss Venezuela",
        "description": "Pollo deshilachado con guacamole, philadelphia, queso mozzarella",
        "ingredients": "Pollo, guacamole, queso philadelphia, queso mozzarella",
        "image": "/static/images/miss_venezuela.png",
        "category": "Brioche's",
        "price": 5.90
    },
    {
        "name": "Old Classic",
        "description": "Queso cheddar, pepinillos, bacon crunch y nuestra salsa burger",
        "ingredients": "Queso cheddar, pepinillos, bacon, salsa",
        "image": "/static/images/old_classic.png",
        "category": "Burger's",
        "price": 9.90
    },
    {
        "name": "Cabramelizada",
        "description": "Empanadilla de queso de cabra, mermelada de tomate, cebolla caramelizada y más queso de cabra",
        "ingredients": "Queso de cabra, mermelada de tomate, cebolla caramelizada",
        "image": "/static/images/cabramelizada.png",
        "category": "Burger's",
        "price": 10.90
    },
    {
        "name": "Phillycheeseburger",
        "description": "Pimientos y cebolla en tempura, bacon crunch y salsa de queso whiz",
        "ingredients": "Pimientos, cebolla, bacon, queso whiz",
        "image": "/static/images/phillycheeseburger.png",
        "category": "Burger's",
        "price": 9.90
    },
    {
        "name": "Rosa del Desierto",
        "description": "Base de pistachos picados con miel y romero, queso mozzarella, queso cheddar, bacon crunch y salsa secret-mayo",
        "ingredients": "Pistachos, miel, romero, queso mozzarella, queso cheddar, bacon, salsa",
        "image": "/static/images/rosa_del_desierto.png",
        "category": "Burger's",
        "price": 10.90
    },
    {
        "name": "La Emmyliana",
        "description": "Patatas pajas, bacon crunch, pepinillos, queso cheddar y salsa emmy",
        "ingredients": "Patatas, bacon, pepinillos, queso cheddar, salsa",
        "image": "/static/images/la_emmyliana.png",
        "category": "Burger's",
        "price": 9.90
    },
    {
        "name": "Sweet Emmy",
        "description": "Patatas pajas, bacon crunch, queso mozzarella, queso cheddar, cebolla caramelizada y salsa sweet emmy",
        "ingredients": "Patatas, bacon, queso mozzarella, queso cheddar, cebolla caramelizada, salsa",
        "image": "/static/images/sweet_emmy.png",
        "category": "Burger's",
        "price": 9.90
    },
    {
        "name": "Foundchesse",
        "description": "Queso cheddar, queso emmental, queso roquefort y salsa de queso whiz envuelta en papel de aluminio",
        "ingredients": "Queso cheddar, queso emmental, queso roquefort, salsa de queso whiz",
        "image": "/static/images/foundchesse.png",
        "category": "Burger's",
        "price": 10.90
    },
    {
        "name": "Burger del Mes",
        "description": "Cada mes nuestro chef nos sorprenderá con una nueva creación",
        "ingredients": "Variable",
        "image": "/static/images/burger_del_mes.png",
        "category": "Burger's",
        "price": 11.90
    },
    {
        "name": "La Hulk",
        "description": "Burger de pollo frito, cebolla crunch, bacon crunch, queso cheddar y guacamole",
        "ingredients": "Pollo frito, cebolla, bacon, queso cheddar, guacamole",
        "image": "/static/images/la_hulk.png",
        "category": "Burger's",
        "price": 8.90
    },
    {
        "name": "EME Tattoo",
        "description": "Burger de pollo frito, quicos picados, cebolla caramelizada, queso de cabra y salsa eme",
        "ingredients": "Pollo frito, quicos, cebolla caramelizada, queso de cabra, salsa",
        "image": "/static/images/eme_tattoo.png",
        "category": "Burger's",
        "price": 8.90
    },
    {
        "name": "Young OG (Niños)",
        "description": "Burger de una patty, queso cheddar y salsa eme",
        "ingredients": "Patty de carne, queso cheddar, salsa",
        "image": "/static/images/young_og.png",
        "category": "Burger's",
        "price": 6.50
    },
    {
        "name": "Tarta del Yayo",
        "description": "Reconstrucción de la clásica tarta del abuelo, con mousse de chocolate jungle, ganache kinder bueno y galleta lotus",
        "ingredients": "Chocolate jungle, kinder bueno, galleta lotus",
        "image": "/static/images/tarta_del_yayo.png",
        "category": "Postres",
        "price": 4.90
    },
    {
        "name": "Tarta de Queso del Mes",
        "description": "Tarta de queso elaborada por nuestro chef que irá variando de sabor mensualmente",
        "ingredients": "Variable",
        "image": "/static/images/tarta_de_queso_del_mes.png",
        "category": "Postres",
        "price": 5.90
    },
    {
        "name": "Las Bravas de la Emilia",
        "description": "Papas de boniato fritos acompañados de nuestra salsa",
        "ingredients": "Papas, boniato, salsa",
        "image": "/static/images/las_bravas_de_la_emilia.png",
        "category": "Entrantes",
        "price": 6.70
    },
    {
        "name": "Patatas EME",
        "description": "Patatas fritas con bacon, cebolla crunch, queso cheddar queso emmental y salsa del EME gratinadas al horno",
        "ingredients": "Patatas, bacon, cebolla, queso cheddar, queso emmental, salsa",
        "image": "/static/images/patatas_eme.png",
        "category": "Entrantes",
        "price": 7.80
    },
    {
        "name": "La Ibérica",
        "description": "Croqueta de jamón 100% ibérico de bellota rebozado en panko",
        "ingredients": "Jamón ibérico, panko",
        "image": "/static/images/la_iberica.png",
        "category": "Entrantes",
        "price": 2.20
    },
    {
        "name": "La Chuletona",
        "description": "Croqueta de chuleta de vaca madurada rebozado en panko",
        "ingredients": "Chuleta de vaca, panko",
        "image": "/static/images/la_chuletona.png",
        "category": "Entrantes",
        "price": 2.50
    },
    {
        "name": "La Pio Pio",
        "description": "Croqueta de pollo asado, trufa y boletus rebozado en panko",
        "ingredients": "Pollo asado, trufa, boletus, panko",
        "image": "/static/images/la_pio_pio.png",
        "category": "Entrantes",
        "price": 2.20
    },
    {
        "name": "El Combo",
        "description": "Combo de nuestras tres croquetas",
        "ingredients": "Variable",
        "image": "/static/images/el_combo.png",
        "category": "Entrantes",
        "price": 6.50
    }
]

# Insertar datos en la base de datos
for item in menu_items:
    conn.execute('''
    INSERT INTO menu_items (name, description, ingredients, image, category, price)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (item["name"], item["description"], item["ingredients"], item["image"], item["category"], item["price"]))

conn.commit()
conn.close()
print("Datos insertados en la base de datos con éxito.")
print("Database created and populated successfully.")
