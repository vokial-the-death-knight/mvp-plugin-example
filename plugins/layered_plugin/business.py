import random
import string
from .persistence import ProductRepository
from .models import Product

class BusinessLogic:
    def __init__(self):
        self.repository = ProductRepository()

    def add_product(self):
        self.repository.initialize_storage()
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        product_name = 'Produkt ' + random_text
        product = Product(name=product_name)
        self.repository.add_product(product)

    def get_all_products(self):
        self.repository.initialize_storage()
        data = self.repository.get_all_products()
        return data
