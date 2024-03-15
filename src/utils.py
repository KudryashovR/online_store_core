import json
import os

from src.Category import Category


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
    Инициализирует список категорий с их продуктами на основе переданного списка категорий.

    Функция проходит по списку категорий, создает экземпляры класса Category для каждой категории,
    добавляет в каждую категорию соответствующие продукты и формирует из этих категорий новый список.

    Аргументы:
        - categories (list): список словарей, где каждый словарь представляет собой категорию с полями:
            'name' (имя категории), 'description' (описание категории) и 'products' (список продуктов).

    Возвращаемое значение:
        - categories_list (list): список объектов Category с добавленными в каждый объект продуктами.
    """

    categories_list = []

    for index, item in enumerate(categories):
        products = item["products"]
        categories_list.append(Category(item["name"], item["description"]))

        for prod in products:
            categories_list[index].add_prod(prod)

    return categories_list
