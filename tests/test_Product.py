from src.Product import Product


def test_product(app_product: Product) -> None:
    """Тест класса Product."""

    assert app_product.name == "Samsung Galaxy S23 Ultra"
    assert app_product.description == "256GB, Серый цвет, 200MP камера"
    assert app_product.price == 180000.0
    assert app_product.quantity == 5


def test_new_product(app_product: Product):
    """Тест класса Product. Добавляем новый продукт"""

    new_product = app_product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price(app_product: Product) -> None:
    """Тест класса Product, модуля price (Изменение цены)."""

    app_product.price = 800
    assert app_product.price == 800


def test_price_error(capsys, app_product: Product) -> None:
    """Тест класса Product, модуля price (Изменение цены если цена <= 0)."""

    app_product.price = 0.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(app_product: Product) -> None:
    """Тест класса Product __str__."""

    assert str(app_product) == "Samsung Galaxy S23 Ultra,  180000.0 руб. Остаток: 5 шт."


def test_product__str(app_product: Product, app_product2) -> None:
    """Тест класса Product __app__."""

    assert app_product + app_product2 == 1000000.0
