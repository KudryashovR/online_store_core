from typing import Union


from src.product import Product, Smartphone, LawnGrass
from src.exceptions import AddZeroQuantityException


class Category:
    """
    Класс Категория для хранения и управления группами продуктов.
    """

    name: str
    description: str
    prod: list
    total_categories: int = 0
    total_unique_products: int

    def __init__(self, name: str, description: str, product: dict = None) -> None:
        """
        Атрибуты:
            - name (str): Название категории.
            - description (str): Описание категории.
            - __prod (list): Приватный список продуктов в категории.
            - total_categories (int): Статический атрибут, общее количество созданных категорий.
            - total_unique_products (int): Количество уникальных продуктов в категории.

            Методы:
            - __init__(self, name, description, product=None): Конструктор для создания объекта категории.
                                                               Принимает название и описание категории, а также
                                                               необязательный словарь prod для добавления первого
                продукта.
            - __repr__(self): Возвращает строковое представление объекта категории для отладки.
            - __str__(self): Возвращает строковое представление объекта категории для пользователя.
            - __len__(self): Возвращает общее количество продуктов в категории.
            - add_prod(self, new_product): Добавляет новый продукт в категорию.
            - product (property): Возвращает информацию о всех продуктах в категории в удобочитаемом формате.
            - prod (property): Геттер для доступа к списку продуктов в категории.
            - avg_price(self): Подсчет среднего ценника товаров в категории.

        Примечание:
            Для добавления продуктов используется метод add_prod. Продукт должен быть объектом класса, поддерживающего
            атрибуты name, description, price и quantity. Эти атрибуты должны быть доступны для чтения.
        """

        self.name = name
        self.description = description
        self.__prod = []

        if product:
            self.__prod.append(Product(product["name"], product["description"], product["price"], product["quantity"]))

        self.total_categories += 1
        self.total_unique_products = len(self.__prod)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта категории для отладки.
        """

        return (f"{self.__class__.__name__}({self.name}, {self.description}, {self.prod})\ntotal_categories: "
                f"{self.total_categories}\ntotal_unique_products: {self.total_unique_products}")

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта категории для пользователя.
        """

        return f"{self.name}, количество продуктов: {len(self)} шт. (Средняя цена: {self.avg_price()} руб.)"

    def __len__(self) -> int:
        """
        Возвращает общее количество продуктов в категории.
        """

        stock_quantity_count = 0

        for item in self.prod:
            stock_quantity_count += item.stock_quantity

        return stock_quantity_count

    def add_prod(self, new_product: Union[Product, Smartphone, LawnGrass]) -> None:
        """
        Добавляет новый продукт в категорию.
        """

        if isinstance(new_product, Product):
            if new_product.stock_quantity == 0:
                raise AddZeroQuantityException()
            else:
                self.__prod.append(new_product)
                self.total_unique_products += 1
        else:
            raise ValueError("Тип добавляемого объекта не соответствует категории")

    @property
    def product(self) -> str:
        """
        Возвращает информацию о всех продуктах в категории в удобочитаемом формате.
        """

        result = ""

        for item in self.__prod:
            result += str(item) + "\n"

        return result.rstrip()

    @property
    def prod(self) -> list:
        """
        Геттер для доступа к списку продуктов в категории.
        """

        return self.__prod

    def avg_price(self):
        """
        Подсчет среднего ценника товаров в категории.
        """

        price_sum = 0
        product_count = 0

        for product in self.prod:
            price_sum += product.price
            product_count += 1

        try:
            result = price_sum / product_count
        except ZeroDivisionError:
            return 0
        else:
            return round(result, 2)


class CategoryIter:
    """
    Итератор для обхода продуктов в категории.
    """

    category_obj: Category
    index: int = -1

    def __init__(self, category_obj: Category) -> None:
        """
        Позволяет итерировать по всем продуктам, принадлежащим к заданной категории,
        используя итерационные протоколы Python.

        Атрибуты:
            category_obj (Category): Объект категории, содержащий продукты.
            index (int): Текущий индекс продукта, который будет возвращен при следующем вызове __next__().

        Параметры:
            category_obj: Экземпляр класса Category, через который будет происходить итерация.

        Методы:
            __iter__(): Возвращает самого себя как итератор.
            __next__(): Возвращает следующий продукт в категории или вызывает StopIteration, если продукты закончились.

        Пример использования:
            category = Category(prod=[Product1, Product2, Product3])
            category_iter = CategoryIter(category)
            for product in category_iter:
                print(product)
        """

        self.category_obj = category_obj

    def __iter__(self) -> 'CategoryIter':
        """
        Возвращает самого себя как итератор.
        """

        return self

    def __next__(self) -> Union[Product, Smartphone, LawnGrass]:
        """
        Возвращает следующий продукт в категории или вызывает StopIteration, если продукты закончились.
        """

        if self.index + 1 < len(self.category_obj.prod):
            self.index += 1

            return self.category_obj.prod[self.index]
        else:
            raise StopIteration
