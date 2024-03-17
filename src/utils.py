import json
import os

from category import Category
from product import Product


def load_products(filename):
    """
    Загружает список продуктов из JSON-файла по указанному имени файла.

    Функция открывает файл, находящийся в папке 'data', читает его содержимое
    и преобразует из формата JSON в Python-структуру данных. В случае успешного выполнения,
    возвращает результат в виде Python-структуры данных (например, списка или словаря).

    Аргументы:
        - filename (str): имя файла (без указания пути к папке 'data'), из которого будет происходить чтение.

    Возвращаемое значение:
        - result: содержимое файла в преобразованном виде (например, список или словарь),
            считанное из JSON-файла.

    Исключения:
        - json.decoder.JSONDecodeError: возникает, когда содержимое файла невозможно
            преобразовать из формата JSON. Исключение перебрасывается
            далее без изменений.

    Примечание:
    Функция требует, чтобы в той же директории, что и программа, присутствовала папка 'data'.
    """

    filepath = os.path.join("data", filename)

    try:
        with open(filepath) as file:
            result = json.loads(file.read())

            return result
    except json.decoder.JSONDecodeError as original_error:
        raise original_error


def category_init(categories):
    """
    Инициализирует и возвращает список категорий с товарами.

    Данная функция принимает список словарей категорий, каждый из которых содержит информацию о категории
    и список продуктов, принадлежащих этой категории. Для каждой категории создается объект класса Category,
    а каждый продукт внутри категории обрабатывается с помощью статического метода check_unique_items класса Product
    для идентификации уникальных продуктов. Затем для каждого уникального продукта создается объект класса Product,
    который добавляется в соответствующую категорию.

    :param categories: Список словарей категорий, где каждый словарь содержит ключи 'name', 'description'
                       и 'products', а 'products' является списком словарей продуктов, каждый из которых содержит
                       'name', 'description', 'price' и 'quantity'.
    :return: Список объектов класса Category, каждый из которых содержит уникальные объекты товаров.
    """

    categories_list = []

    for index, item in enumerate(categories):
        products = item["products"]
        categories_list.append(Category(item["name"], item["description"]))
        products = Product.check_unique_items(products)

        for prod in products:
            categories_list[index].add_prod(Product.create_product(prod))

    return categories_list
