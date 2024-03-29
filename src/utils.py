import json
import os

from src.category import Category, CategoryIter
from src.product import Product, Smartphone, LawnGrass
from src.order import Order


def load_products(filename: str) -> dict:
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

    filepath = os.path.join("src/data", filename)

    try:
        with open(filepath) as file:
            result = json.loads(file.read())

            return result
    except json.decoder.JSONDecodeError as original_error:
        raise original_error


def category_init(categories: dict) -> list:
    """
    Инициализирует и возвращает список категорий, каждая из которых включает в себя уникальные продукты.

    Принимает на вход список категорий, где каждая категория представлена словарем с ключами 'name' (название
    категории), 'description' (описание категории) и 'products' (список продуктов, принадлежащих к категории). Каждый
    продукт в списке также представляется словарем с необходимыми атрибутами для создания соответствующего объекта
    продукта (например, 'name', 'description', 'price', 'quantity' и дополнительные атрибуты в зависимости от типа
    продукта).

    Для каждой категории создается объект класса Category. Продукты в каждой категории проверяются на уникальность
    с помощью статического метода check_unique_items класса Product. Для каждого уникального продукта определяется его
    тип и на основании этого создается соответствующий объект (например, Smartphone или LawnGrass) с помощью
    классового метода create_product. Созданные объекты продуктов добавляются в свои категории.

    :param categories: Список словарей, представляющих категории. Каждый словарь содержит ключи 'name' и 'description'
                       для категории и 'products' — список словарей продуктов. Продукты имеют атрибуты, необходимые
                       для их идентификации и создания объектов соответствующих классов.
    :return: Список объектов класса Category, в котором каждый объект содержит список уникальных продуктов,
             соответствующих данной категории и добавленных с учетом их спецификации (например, тип продукта).
    """

    categories_list = []

    for index, item in enumerate(categories):
        products = item["products"]
        categories_list.append(Category(item["name"], item["description"]))
        products = Product.check_unique_items(products)

        for prod in products:
            match item["name"]:
                case "Смартфоны":
                    categories_list[index].add_prod(Smartphone.create_product(prod))
                case "Трава газонная":
                    categories_list[index].add_prod(LawnGrass.create_product(prod))
                case _:
                    categories_list[index].add_prod(Product.create_product(prod))

    return categories_list


def print_statistics(categories_list: list) -> None:
    """
    Печатает статистику по каждой категории и выводит сумму стоимости товаров в каждой категории.

    Данная функция принимает список категорий, итерирует по каждой категории, печатая ее содержимое,
    затем рассчитывает и печатает сумму стоимости товаров в каждой категории.

    Параметры:
        categories_list (list): Список категорий, для каждой из которых будет выведена статистика.

    Процесс работы функции:
    1. Итерирует по каждому элементу `categories_list`, печатая его (предполагается, что это объект категории).
    2. Использует класс `CategoryIter` для итерации по товарам каждой категории и печатает их.
    3. Рассчитывает сумму стоимости товаров в каждой категории. Если количество товаров больше одного,
       суммирует значения, предполагая что у объектов товара есть числовые значения, которые можно суммировать.
       Если товар один, просто присваивается значение цены этого товара.
    4. Выводит общую сумму стоимости товаров в категории.

    Примечание:
    - Есть предположение, что каждая категория представлена объектом, имеющим атрибут `prod`, список товаров,
      а сами товары имеют атрибут `price` для суммирования.
    - Функция рассчитана на работу с конкретной структурой данных и может потребовать модификации для
      соответствия реальным объектам и их структурам.

    Пример использования:
        categories_list = [Category1, Category2]
        print_statistics(categories_list)
    """

    for item in categories_list:
        print(item)

        for prod in CategoryIter(item):
            print(prod)

        prod_sum = 0

        if len(item.prod) - 1 != 0:
            for index in range(len(item.prod) - 1):
                prod_sum += item.prod[index] + item.prod[index + 1]
        else:
            prod_sum = item.prod[0].price

        print(f"Всего товаров на сумму: {prod_sum}")

        print()


def change_price(categories_list: list, change_price_name: str) -> None:
    """
    Изменяет цену указанного товара в списках категорий.

    Данная функция выполняет поиск в предоставленном списке категорий для нахождения товара с указанным именем.
    Если такой товар находится, функция предлагает пользователю ввести новую цену и обновляет цену найденного товара.
    В случае если товар с указанным именем не найден в ни одной из категорий, выводится сообщение о том,
    что товар не найден.

    Параметры:
        categories_list (list): Список категорий, каждая из которых содержит список товаров.
        change_price_name (str): Имя товара, цену на который необходимо изменить.

    Примечание:
    - Предполагается, что каждый товар в списке имеет атрибут `name` по которому вы можете идентифицировать товар,
      и атрибут `price` который представляет собой цену товара и может быть изменен.
    - Также как и в предыдущих примерах предполагается использование класса `CategoryIter` для итерации товаров
      в каждой категории.

    Пример использования:
        categories = [Category1, Category2]
        change_price_name = "ТоварНазвание"
        change_price(categories, change_price_name)

    После вызова функции страница:
    - Если товар с указанным именем найден, пользователю будет предложено ввести новую цену для обновления.
    - Если товар не найден, будет выведено сообщение "Указанный товар не найден".
    """

    is_find = False

    for item in categories_list:
        for prod in CategoryIter(item):
            if prod.name == change_price_name:
                is_find = True

                new_price = float(input("Введите новую цену товара: "))

                prod.price = new_price

    if not is_find:
        print("Указанный товар не найден")

    print()


def print_operations() -> str:
    print("\033[34m{}".format("Операции:"))
    print("1. Изменение цены продукта")
    print("2. Подготовка заказа для покупки товара")

    mode = input("\033[34m{}\033[0m".format("Введите номер операции или оставьте поле пустым для выхода "
                                            "из программы: "))

    return mode


def get_order(categories_list: list, buying_product_name: str) -> None:
    buying_product_quantity = int(input("\033[34m{}\033[0m".format("Введите количество покупаемого "
                                                                   "товара: ")))

    for item in categories_list:
        for prod in CategoryIter(item):
            if prod.name == buying_product_name:
                print()
                print("\033[31m{}\033[0m".format(Order(prod, buying_product_quantity)))
                print()
