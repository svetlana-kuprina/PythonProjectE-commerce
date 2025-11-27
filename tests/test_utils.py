import json
from unittest.mock import mock_open, patch

from src.utils import object_from_json, open_json


@patch("builtins.open", new_callable=mock_open)
def test_open_json(mock_open_json) -> None:
    """Тест функции принимает на вход путь до JSON-файла и возвращает список словарей
    с данными. Используется Mock и patch"""

    data_mock = [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]

    mock_file = mock_open_json.return_value
    mock_file.read.return_value = json.dumps(data_mock)
    assert open_json("test.json") == data_mock


def test_object_from_json() -> None:
    """Тест функции object_from_json принимает список словарей и возвращает объекты классов"""

    test_list = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
    expected = object_from_json(test_list)
    assert expected[0].name == "Смартфоны"
    assert expected[0].products[0].name == "Samsung Galaxy C23 Ultra"
