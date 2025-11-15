from typing import List

from src.Product import Product


class Category:
    """Класс обрабатывает категории товаров"""

    name: str
    description: str
    products: List[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        Category.product_count = len(products)
        Category.category_count += 1
