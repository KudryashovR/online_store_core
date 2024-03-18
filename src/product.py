class Product:
    """
    Класс Продукт представляет сущность товара на складе или в магазине.
    """

    name: str
    description: str
    price: float
    stock_quantity: int

    def __init__(self, name, description, price, stock_quantity):
        """
        Атрибуты:
            - name (str): Название продукта.
            - description (str): Описание продукта.
            - price (float): Цена продукта. Доступно только для чтения через декоратор property.
            - stock_quantity (int): Количество товара на складе.

        Методы:
            - __init__(self, name, description, price, stock_quantity): Конструктор класса. Создает экземпляр товара
                с заданными параметрами.
            - __repr__(self): Возвращает строковое представление продукта для отладки.
            - __str__(self): Возвращает строковое представление продукта для пользователя.
            - create_product(cls, name, description, price, stock_quantity): Классовый метод для создания и возвращения
                нового экземпляра продукта.
            - check_unique_items(products): Статический метод для проверки списка продуктов на уникальность исходя
                из их имени и корректного подсчета общего количества и максимальной цены для одинаковых имён продуктов.
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

    def __repr__(self):
        """
        Возвращает строковое представление продукта для отладки.
        """

        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.stock_quantity})"

    def __str__(self):
        """
        Возвращает строковое представление продукта для пользователя.
        """

        return f"{self.name}, {self.price} руб. Остаток: {self.stock_quantity} шт."

    @classmethod
    def create_product(cls, prod):
        """
        Создает и возвращает новый экземпляр класса Product.

        :param prod: словарь с характеристиками товара.
        :return: Экземпляр класса Product.
        """

        return cls(prod["name"], prod["description"], prod["price"], prod["quantity"])

    @staticmethod
    def check_unique_items(products):
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
                    unique_names[index]["quantity"] += item["quantity"]
                    break

            if is_unique:
                unique_names.append(prod)

        return unique_names

    @property
    def price(self):
        """
        Возвращает цену продукта.

        :return: Цена продукта.
        """

        return self.__price

    @price.setter
    def price(self, new_price):
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
    def stock_quantity(self):
        """
        Возвращает количество продукта.
        """

        return self.__stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, new_stock_quantity):
        """
        Устанавливает новое количество продукта.

        :param new_stock_quantity: Новое количество продукта.
        """

        self.__stock_quantity = new_stock_quantity
