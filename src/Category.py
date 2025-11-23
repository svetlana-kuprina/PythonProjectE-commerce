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
        self.__products = products

        Category.product_count = len(products)
        Category.category_count += 1

    @property
    def products(self) -> List[Product]:
        """Геттер для списка продуктов. Возвращает список"""

        return self.__products

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count = len(self.__products)

    @property
    def products_str(self) -> str:
        """Геттер для списка продуктов. Возвращает строку вида: Название продукта, 80 руб. Остаток: 15 шт."""

        product_str = ""
        for product in self.__products:
            product_str += f"{product.name},  {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
