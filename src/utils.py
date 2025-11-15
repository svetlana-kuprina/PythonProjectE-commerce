import json
import os
from typing import List, Any

from src.Category import Category
from src.Product import Product


def open_json(path: str) ->  Any:
    """Функция читает json файл и записывает его как список словарей"""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def object_from_json(data: list[dict]) -> list[Category]:
    """Функция создает объекты классов из списка словарей."""

    category = []
    for cat in data:
        product = []
        for prod in cat["products"]:
            product.append(Product(**prod))
            cat["products"] = product
        category.append(Category(**cat))
    return category
