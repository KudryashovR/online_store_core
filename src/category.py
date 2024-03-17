from product import Product


class Category:
    """
    Класс Категория для хранения и управления группами продуктов.
    """

    name: str
    description: str
    __prod: list
    total_categories: int = 0
    total_unique_products: int

    def __init__(self, name, description, prod=None):
        """
        Атрибуты:
            - name (str): Название категории.
            - description (str): Описание категории.
            - __prod (list): Приватный список продуктов в категории.
            - total_categories (int): Статический атрибут, общее количество созданных категорий.
            - total_unique_products (int): Количество уникальных продуктов в категории.

            Методы:
            - __init__(self, name, description, prod=None): Конструктор для создания объекта категории.
                Принимает название и описание категории, а также необязательный словарь prod для добавления первого
                продукта.
            - __repr__(self): Возвращает строковое представление объекта категории.
            - add_prod(self, new_product): Добавляет новый продукт в категорию.
            - product (property): Возвращает информацию о всех продуктах в категории в удобочитаемом формате.
            - prod (property): Геттер для доступа к списку продуктов в категории.

        Примечание:
            Для добавления продуктов используется метод add_prod. Продукт должен быть объектом класса, поддерживающего
            атрибуты name, description, price и quantity. Эти атрибуты должны быть доступны для чтения.
        """

        self.name = name
        self.description = description
        self.__prod = []

        if prod:
            self.__prod.append(Product(prod["name"], prod["description"], prod["price"], prod["quantity"]))

        self.total_categories += 1
        self.total_unique_products = len(self.__prod)

    def __repr__(self):
        """
        Возвращает строковое представление объекта категории.
        """

        return (f"Название: {self.name}\nОписание: {self.description}\nТовары: {self.__prod}\nОбщее количество "
                f"категорй: {self.total_categories}\nОбщее количество уникальных "
                f"продуктов: {self.total_unique_products}")

    def add_prod(self, new_product):
        """
        Добавляет новый продукт в категорию.
        """

        self.__prod.append(new_product)
        self.total_unique_products += 1

    @property
    def product(self):
        """
        Возвращает информацию о всех продуктах в категории в удобочитаемом формате.
        """

        result = ""

        for item in self.__prod:
            result += f"{item.name}, {item.price} руб. Остаток: {item.stock_quantity} шт.\n"

        return result.rstrip()

    @property
    def prod(self):
        """
        Геттер для доступа к списку продуктов в категории.
        """

        return self.__prod
