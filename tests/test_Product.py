from src.Product import Product


def test_product(app_product: Product) -> None:
    """Тест класса Product."""

    assert app_product.name == "Samsung Galaxy S23 Ultra"
    assert app_product.description == "256GB, Серый цвет, 200MP камера"
    assert app_product.price == 180000.0
    assert app_product.quantity == 5


def test_new_product(app_product: Product):
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
