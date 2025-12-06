from abc import ABC, abstractmethod
from typing import Any, Dict

from src.MixinRepr import MixinRepr


class BaseProduct(ABC):
    """Абстрактный класс для класса Product"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass


class Product(BaseProduct, MixinRepr):
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
        MixinRepr.__init__(self)

    def __str__(self) -> str:
        """Строковое отображение в следующем виде: Название продукта, XX руб. Остаток: XX шт."""

        return f"{self.name},  {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> int:
        """Реализована возможность складывать товары."""

        if type(other) is self.__class__:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_prod: Dict) -> "Product":
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


class Smartphone(Product):
    """Класс обрабатывает информацию о продукте категории товаров Смартфон"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс обрабатывает информацию о продукте категории товаров Трава газонная"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
