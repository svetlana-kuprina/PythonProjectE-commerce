def test_product(app_product):
    assert app_product.name == "Samsung Galaxy S23 Ultra"
    assert app_product.description == "256GB, Серый цвет, 200MP камера"
    assert app_product.price == 180000.0
    assert app_product.quantity == 5
