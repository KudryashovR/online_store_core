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
                f"категорй: {self.total_categories}\nОбщее количество уникальных  продуктов{self.total_unique_products}")


if __name__ == "__main__":
    products = {"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
                "quantity": 5}
    test = Category("Смартфоны", "Смартфоны", products)
    print(test)
