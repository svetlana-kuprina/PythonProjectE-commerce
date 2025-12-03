import pytest

from src.Category import Category, ProductCategoryIter
from src.Product import Product


@pytest.fixture
def app_product() -> Product:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return product1


@pytest.fixture
def app_product2() -> Product:
    product2 = Product("Samsung Galaxy", "256GB, Серый цвет, 200MP камера", 100000.0, 1)
    return product2


@pytest.fixture
def app_product_category() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )


@pytest.fixture
def category_iter(app_product_category) -> ProductCategoryIter:
    return ProductCategoryIter(app_product_category)
