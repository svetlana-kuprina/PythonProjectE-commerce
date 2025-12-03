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

    def __str__(self):
        """Строковое отображение в следующем виде: Название категории, количество продуктов: XXX шт."""

        summ_prod = 0
        for prod in self.__products:
            summ_prod += prod.quantity
        return f"{self.name}, количество продуктов: {summ_prod} шт."

    @property
    def products(self) -> List[Product]:
        """Геттер для списка продуктов. Возвращает список"""

        return self.__products

    def add_product(self, product: Product):
        """Модуль реализующий добавление продуктов"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count = len(self.__products)
        else:
            raise TypeError

    @property
    def products_str(self) -> str:
        """Геттер для списка продуктов. Возвращает строку вида: Название продукта, 80 руб. Остаток: 15 шт."""

        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str


class ProductCategoryIter:
    def __init__(self, category_obj: Category):
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self):
        """ Итератор возвращать очередной товар категории."""

        self.index = 0
        return self

    def __next__(self):
        """производить итерацию по товарам"""

        if self.index < len(self.category_obj.products):
            product = self.category_obj.products[self.index]
            self.index += 1
            return product
        else:
            return StopIteration
