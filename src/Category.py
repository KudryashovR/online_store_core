from src.Product import Product


class Category:
    name: str
    description: str
    prod: list
    total_categories: int = 0
    total_unique_products: int

    def __init__(self, name, description, prod=None):
        self.name = name
        self.description = description
        self.prod = []

        if prod:
            self.prod.append(Product(prod["name"], prod["description"], prod["price"], prod["quantity"]))

        self.total_categories += 1
        self.total_unique_products = len(self.prod)

    def __repr__(self):
        return (f"Название: {self.name}\nОписание: {self.description}\nТовары: {self.prod}\nОбщее количество "
                f"категорй: {self.total_categories}\nОбщее количество уникальных "
                f"продуктов{self.total_unique_products}")

    def add_prod(self, value):
        self.prod.append(Product(value["name"], value["description"], value["price"], value["quantity"]))
