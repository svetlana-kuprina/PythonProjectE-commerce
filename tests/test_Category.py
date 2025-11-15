def test_app_product_category(app_product_category):
    assert app_product_category.name == "Смартфоны"
    assert (
        app_product_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert app_product_category.category_count == 1
    assert app_product_category.product_count == 1
