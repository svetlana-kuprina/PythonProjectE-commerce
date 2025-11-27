from typing import Any, Dict


class Product:
    """Класс обрабатывает информацию о продукте"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_prod: Dict):
        """Класс-метод добавления нового продукта"""
        return cls(new_prod["name"], new_prod["description"], new_prod["price"], new_prod["quantity"])

    @property
    def price(self):
        """Геттер приватного атрибута цена"""
        return self.__price

    @price.setter
    def price(self, value: float) -> Any:
        """Сеттер приватного атрибута цена с проверкой цены на 0 и отрицательность"""
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")
