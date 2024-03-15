class Product:
    name: str
    description: str
    price: float
    stock_quantity: int

    def __init__(self, name, description, price, stock_quantity):
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return (f"Название: {self.name}\nОписание: {self.description}\nЦена: {self.price}\nКоличество в "
                f"наличии: {self.stock_quantity}")
