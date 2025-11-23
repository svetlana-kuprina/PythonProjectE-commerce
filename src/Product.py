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
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Геттер приватного атрибута цена"""

        return self.__price

    @price.setter
    def price(self, value):
        """ Сеттер приватного атрибута цена с проверкой цены на 0 и отрицательность"""

        if value <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = value
