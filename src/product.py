from typing import Union
from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @classmethod
    @abstractmethod
    def create_product(cls, prod: dict):
        pass


class Product(AbstractProduct):
    """
    Класс Продукт представляет сущность товара на складе или в магазине.
    """

    name: str
    description: str
    price: float
    stock_quantity: int
    color: str

    def __init__(self, name: str, description: str, price: float, stock_quantity: int, color: str = None) -> None:
        """
        Атрибуты:
            - name (str): Название продукта.
            - description (str): Описание продукта.
            - price (float): Цена продукта. Доступно только для чтения через декоратор property.
            - stock_quantity (int): Количество товара на складе.
            - color (str): Цвет товара (необязательный атрибут).

        Методы:
            - __init__(self, name, description, price, stock_quantity): Конструктор класса. Создает экземпляр товара
                                                                        с заданными параметрами.
            - __repr__(self): Возвращает строковое представление продукта для отладки.
            - __str__(self): Возвращает строковое представление продукта для пользователя.
            - __add__(self, other): Возвращает результирующую сумму (с учетом количества на складе) 2-х объектов типа
                                    Product.
            - create_product(cls, name, description, price, stock_quantity): Классовый метод для создания и возвращения
                                                                             нового экземпляра продукта.
            - check_unique_items(products): Статический метод для проверки списка продуктов на уникальность исходя
                                            из их имени и корректного подсчета общего количества и максимальной цены
                                            для одинаковых имён продуктов.
            - price: Декоратор property для получения цены продукта.
            - price(new_price): Декоратор setter для установки цены продукта. Позволяет установить новую цену с учетом
                                условий валидации.
            - stock_quantity: Декоратор property для получения количествf продукта.
            - stock_quantity(new_stock_quantity): Декоратор setter для установки количества продукта.

        Примечание:
            Важно учитывать, что при изменении цены продукта через сеттер осуществляется проверка на корректность
            введенной цены и подтверждение операции в случае понижения цены.
        """

        self.name = name
        self.description = description
        self.__price = price
        self.__stock_quantity = stock_quantity
        self.color = color

    def __repr__(self) -> str:
        """
        Возвращает строковое представление продукта для отладки.
        """

        return (f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.stock_quantity}, "
                f"{self.color})")

    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта для пользователя.
        """

        return f"{self.name}, {self.price} руб. Остаток: {self.stock_quantity} шт."

    def __add__(self, other: Union['Product', 'Smartphone', 'LawnGrass']) -> float:
        """
        Возвращает результирующую сумму (с учетом количества на складе) 2-х объектов типа Product.
        """

        if type(other) is type(self):
            return self.stock_quantity * self.price + other.stock_quantity * other.price
        else:
            raise ValueError("Типы складываемых объектов не совпадают")

    @classmethod
    def create_product(cls, prod: dict) -> 'Product':
        """
        Создает и возвращает новый экземпляр класса Product.

        :param prod: словарь с характеристиками товара.
        :return: Экземпляр класса Product.
        """

        return cls(prod["name"], prod["description"], prod["price"], prod["quantity"])

    @staticmethod
    def check_unique_items(products: list) -> list:
        """
        Проверяет список продуктов на уникальность исходя из их имени.

        :param products: Список словарей продуктов с ключами 'name', 'price', 'quantity'.
        :return: Список словарей уникальных продуктов с обновленными значениями цены и quantity.
        """

        unique_names = []

        for prod in products:
            is_unique = True

            for index, item in enumerate(unique_names):
                if item["name"] == prod["name"]:
                    is_unique = False
                    unique_names[index]["price"] = max(item["price"], prod["price"])
                    unique_names[index]["quantity"] += prod["quantity"]
                    break

            if is_unique:
                unique_names.append(prod)

        return unique_names

    @property
    def price(self) -> float:
        """
        Возвращает цену продукта.

        :return: Цена продукта.
        """

        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Устанавливает новую цену продукта с предварительной валидацией.

        :param new_price: Новая цена продукта.
        """

        if new_price <= 0:
            print("Введена некоректная цена")
        elif new_price < self.price:
            user_answer = input("Новая цена ниже установленной. Подтвердите операцию [y/N]: ")

            if user_answer.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @property
    def stock_quantity(self) -> int:
        """
        Возвращает количество продукта.
        """

        return self.__stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, new_stock_quantity: int) -> None:
        """
        Устанавливает новое количество продукта.

        :param new_stock_quantity: Новое количество продукта.
        """

        self.__stock_quantity = new_stock_quantity


class Smartphone(Product):
    """
    Класс, представляющий смартфон как продукт.

    Этот класс наследуется от класса Product и добавляет специфичные для смартфона характеристики,
    такие как эффективность, название модели и внутренняя память.
    """

    efficiency: float
    model_name: str
    internal_memory: float

    def __init__(self, name: str, description: str, price: float, stock_quantity: int, color: str,
                 efficiency: float, model_name: str, internal_memory: float) -> None:
        """
        Атрибуты:
            efficiency (float): Эффективность смартфона, возможно, это может быть мера производительности
                                или энергоэффективности.
            model_name (str): Название модели смартфона.
            internal_memory (float): Размер внутренней памяти смартфона в гигабайтах.

        Параметры конструктора (__init__):
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            stock_quantity (int): Количество продукта на складе.
            efficiency (float): Эффективность смартфона.
            model_name (str): Название модели смартфона.
            internal_memory (float): Внутренняя память смартфона.
            color (str): Цвет смартфона.

        Методы:
            __repr__: Возвращает строковое представление объекта класса Smartphone.

        Классовые методы:
            create_product(cls, prod): Создает и возвращает объект класса Smartphone из полученного словаря параметров
                                       prod.
        """

        super().__init__(name, description, price, stock_quantity, color)
        self.efficiency = efficiency
        self.model_name = model_name
        self.internal_memory = internal_memory

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта класса Smartphone.

        Возвращаемое значение:
            str: Строковое представление объекта.
        """

        return (f"Parent: {super().__class__.__name__}\n{self.__class__.__name__}({self.name}, {self.description}, "
                f"{self.price}, {self.stock_quantity}, {self.efficiency}, {self.model_name}, {self.internal_memory}, "
                f"{self.color})")

    @classmethod
    def create_product(cls, prod: dict) -> 'Smartphone':
        """
        Создает и возвращает объект класса Smartphone из полученного словаря параметров prod.

        Параметры:
            prod (dict): Словарь параметров с ключами, соответствующими атрибутам класса Smartphone.

        Возвращаемое значение:
            Smartphone: Объект класса Smartphone.
        """

        return cls(prod["name"], prod["description"], prod["price"], prod["quantity"], prod["color"],
                   prod["efficiency"], prod["model_name"], prod["internal_memory"])


class LawnGrass(Product):
    """
    Класс, представляющий семена газонной травы как продукт.

    Этот класс наследуется от базового класса Product и добавляет уникальные характеристики газонной травы,
    такие как страна происхождения и период прорастания.
    """

    origin_country: str
    germination_period: int

    def __init__(self, name: str, description: str, price: float, stock_quantity: int, color: str,
                 origin_country: str, germination_period: int) -> None:
        """
        Атрибуты:
            origin_country (str): Страна происхождения семян газонной травы.
            germination_period (int): Время, необходимое для прорастания семян газонной травы (в днях).

        Параметры конструктора (__init__):
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            stock_quantity (int): Количество продукта на складе.
            origin_country (str): Страна происхождения семян газонной травы.
            germination_period (int): Период прорастания семян газонной травы.
            color (str): Цвет упаковки или семян.

        Методы:
            __repr__: Возвращает строковое представление объекта класса LawnGrass.

        Классовые методы:
            create_product(cls, prod): Создает и возвращает объект класса LawnGrass из полученного словаря параметров
                                       prod.
        """

        super().__init__(name, description, price, stock_quantity, color)
        self.origin_country = origin_country
        self.germination_period = germination_period

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта класса LawnGrass.

        Возвращаемое значение:
            str: Строковое представление объекта.
        """

        return (f"Parent: {super().__class__.__name__}\n{self.__class__.__name__}({self.name}, {self.description}, "
                f"{self.price}, {self.stock_quantity}, {self.origin_country}, {self.germination_period}, "
                f"{self.color})")

    @classmethod
    def create_product(cls, prod: dict) -> 'LawnGrass':
        """
        Создает и возвращает объект класса LawnGrass из полученного словаря параметров prod.

        Параметры:
            prod (dict): Словарь параметров с ключами, соответствующими атрибутам класса LawnGrass.

        Возвращаемое значение:
            LawnGrass: Объект класса LawnGrass.
        """

        return cls(prod["name"], prod["description"], prod["price"], prod["quantity"], prod["color"],
                   prod["origin_country"], prod["germination_period"])
