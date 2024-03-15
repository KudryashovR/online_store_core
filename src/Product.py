class Product:
    """
    Класс, представляющий продукт с его основными характеристиками.

    Этот класс используется для создания объектов продуктов с их названием, описанием, ценой и количеством на складе.
    """

    name: str
    description: str
    price: float
    stock_quantity: int

    def __init__(self, name, description, price, stock_quantity):
        """
        Атрибуты:
            - name (str): Название продукта.
            - description (str): Описание продукта, включающее ключевые характеристики или преимущества.
            - price (float): Цена продукта. Указывается в условных единицах.
            - stockquantity (int): Количество единиц товара, доступного на складе.

        Методы:
            - init(self, name, description, price, stockquantity): Конструктор класса.
                Инициализирует новый экземпляр продукта с заданными значениями параметров.

            - repr(self): Магический метод для представления объекта в виде строки.
                Возвращает строку, описывающую продукт, включая его название, описание, цену и количество на складе.

        Пример использования:
            apple = Product("Apple", "Fresh green apple", 0.5, 100)
            print(apple)

        Вывод:
            Название: Apple
            Описание: Fresh green apple
            Цена: 0.5
            Количество в наличии: 100
        """

        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        """
        Магический метод для представления объекта в виде строки. Возвращает строку, описывающую продукт, включая
        его название, описание, цену и количество на складе.
        """

        return (f"Название: {self.name}\nОписание: {self.description}\nЦена: {self.price}\nКоличество в "
                f"наличии: {self.stock_quantity}")
