import sqlite3
import os

class DatabaseConnection:
    def __init__(self):
        plugin_dir = os.path.dirname(__file__)
        db_path = os.path.join(plugin_dir, 'plugin_database.db')
        self.connection = sqlite3.connect(db_path)

    def create_products_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_product(self, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO products (name) VALUES (?)", (name,))
        self.connection.commit()

    def get_all_products(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM products")
        return cursor.fetchall()

    def close(self):
        self.connection.close()
