import json
import os

from src.Category import Category


def load_products(filename):
    filepath = os.path.join("data", filename)

    try:
        with open(filepath) as file:
            result = json.loads(file.read())

            return result
    except json.decoder.JSONDecodeError as original_error:
        raise original_error


def category_init(categories):
    categories_list = []

    for index, item in enumerate(categories):
        products = item["products"]
        categories_list.append(Category(item["name"], item["description"]))

        for prod in products:
            categories_list[index].add_prod(prod)

    return categories_list
