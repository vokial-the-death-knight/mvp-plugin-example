from .database import DatabaseConnection

class ProductRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def initialize_storage(self):
        self.db.create_products_table()

    def add_product(self, product):
        self.db.insert_product(product.name)

    def get_all_products(self):
        return self.db.get_all_products()
