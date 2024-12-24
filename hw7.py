
import sqlite3

# Создание базы данных и таблицы
def create_db():
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

# Функция для добавления товаров
def add_products():
    products = [
        ('Жидкое мыло', 50.0, 20), ('Мыло детское', 30.0, 50),
        ('Шампунь', 120.0, 15), ('Гель для душа', 80.0, 10),
        ('Зубная паста', 40.0, 25), ('Туалетная бумага', 20.0, 100)
    ]
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()

# Обновление количества товара
def update_quantity(id, quantity):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, id))
    conn.commit()
    conn.close()

# Обновление цены товара
def update_price(id, price):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.execute('UPDATE products SET price = ? WHERE id = ?', (price, id))
    conn.commit()
    conn.close()

# Удаление товара
def delete_product(id):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Печать всех товаров
def print_all_products():
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    for row in c.fetchall():
        print(row)
    conn.close()

# Печать товаров по цене и количеству
def print_under_price_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (price_limit, quantity_limit))
    for row in c.fetchall():
        print(row)
    conn.close()

# Поиск товаров по названию
def search_by_name(keyword):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + keyword + '%',))
    for row in c.fetchall():
        print(row)
    conn.close()

# Вызов функций
create_db()
add_products()
print("Все товары:")
print_all_products()
update_quantity(1, 50)
update_price(2, 35.0)
delete_product(3)
print("\nОбновленные товары:")
print_all_products()
print("\nТовары дешевле 100 и больше 5 на складе:")
print_under_price_quantity(100, 5)
print("\nПоиск товара по слову 'мыло':")
search_by_name('мыло')
