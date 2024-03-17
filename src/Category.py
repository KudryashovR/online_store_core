from Product import Product


class Category:
    """
    Класс, представляющий категорию товаров.
    """

    name: str
    description: str
    __prod: list
    total_categories: int = 0
    total_unique_products: int

    def __init__(self, name, description, prod=None):
        """
        Атрибуты класса:
            - totalcategories (int): хранит общее количество созданных экземпляров категорий.
            - totaluniqueproducts (int): количество уникальных продуктов в конкретной категории.

        Атрибуты экземпляра:
            - name (str): имя категории.
            - description (str): описание категории.
            - prod (list): список продуктов в категории. Каждый продукт представлен экземпляром класса Product.

        Методы:
            - init(self, name, description, prod=None): Конструктор для инициализации нового объекта категории.
                Принимает имя и описание категории. Параметр 'prod' - необязательный и предназначен для инициализации
                списка продуктов одним продуктом (словарь с ключами "name", "description", "price", "quantity").
                Если 'prod' передается, добавляет эти данные в список продуктов категории.

            - repr(self): Магический метод для получения строкового представления объекта. Возвращает информацию
                о категории, включая её имя, описание, перечень продуктов, общее количество категорий и общее количество
                уникальных продуктов.

            - addprod(self, value): Добавляет продукт в категорию. Продукт представляется и передается как словарь
                с ключами "name", "description", "price", "quantity". Создает новый экземпляр класса Product
                с использованием этих данных и добавляет его в список 'prod'.

            Примечания:
                - При создании каждого нового экземпляра категории счетчик 'totalcategories' увеличивается,
                    отражая общее количество созданных категорий.
                - Количество уникальных продуктов в категории 'totaluniqueproducts' обновляется при каждом
                    добавлении продукта через метод addprod.
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
        Магический метод для получения строкового представления объекта. Возвращает информацию о категории, включая
        её имя, описание, перечень продуктов, общее количество категорий и общее количество уникальных продуктов.
        """

        return (f"Название: {self.name}\nОписание: {self.description}\nТовары: {self.__prod}\nОбщее количество "
                f"категорй: {self.total_categories}\nОбщее количество уникальных "
                f"продуктов: {self.total_unique_products}")

    def add_prod(self, new_product):
        """
        Добавляет продукт в категорию. Продукт представляется и передается как словарь с ключами "name", "description",
        "price", "quantity". Создает новый экземпляр класса Product с использованием этих данных и добавляет
        его в список 'prod'.
        """

        self.__prod.append(new_product)
        self.total_unique_products += 1

    @property
    def product(self):
        result = ""

        for item in self.__prod:
            result += f"{item.name}, {item.price} руб. Остаток: {item.stock_quantity} шт.\n"

        return result.rstrip()

    @property
    def prod(self):
        return self.__prod
