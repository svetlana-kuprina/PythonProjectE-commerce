from src.Category import Category
from src.Product import Product


def test_app_product_category(app_product_category: Category) -> None:
    """Тест класса Category"""

    assert app_product_category.name == "Смартфоны"
    assert (
        app_product_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


def test_products(app_product_category: Category) -> None:
    """Тест класса Category, геттера products"""

    assert app_product_category.name == "Смартфоны"
    assert (
        app_product_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


def test_add_product(app_product_category: Category) -> None:
    """Тест класса Category, модуля add_product"""

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    app_product_category.add_product(product4)
    assert app_product_category.name == "Смартфоны"
    assert (
        app_product_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert app_product_category.products[1] == product4


def test_products_str(app_product_category: Category) -> None:
    """Тест класса Category, геттера products"""

    assert app_product_category.products_str == "Samsung Galaxy S23 Ultra,  180000.0 руб. Остаток: 5 шт.\n"
