import pytest

from src.Category import Category, ProductCategoryIter
from src.Product import Product, Smartphone, LawnGrass


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

@pytest.fixture
def smartphone () -> Smartphone:
    product1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    return product1

@pytest.fixture
def lawngrass()-> LawnGrass:
    product1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return product1
