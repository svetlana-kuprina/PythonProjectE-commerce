class MixinRepr:
    """Миксин печатает в консоль информацию об объекте при инициализации
    'Продукт1', 'Описание продукта', 1200, 10"""

    def __init__(self) -> None:
        """Вывод repr в консоль"""

        print(repr(self))

    def __repr__(self) -> str:
        """Вывод информации о продукте при создании объекта класса вида:
        'Продукт1', 'Описание продукта', 1200, 10"""

        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"
