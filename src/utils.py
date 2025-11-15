import json
import os

from src.Category import Category
from src.Product import Product


def open_json(path: str):
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as json_file:
        return json.load(json_file)

def object_from_json(data:list[dict]):
    category = []
    for cat in data:
        product = []
        for prod in cat["products"]:
            product.append(Product(**prod))
            cat["products"] = product
        category.append(Category(**cat))
    return category

if __name__ == "__main__":
   data_json = open_json("../data/products.json")
   print(data_json)
   ob = object_from_json(data_json)
   print(ob[0].name)
   print(ob[0].products[0].name)