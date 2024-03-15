class Category:
    name: str
    description: str
    products: list
    total_categories: int = 0
    total_unique_products: int

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description

        if products:
            self.products = products
        else:
            self.products = []

        self.total_categories += 1
        self.total_unique_products = len(set(products))

    def __repr__(self):
        return (f"Название: {self.name}\nОписание: {self.description}\nТовары: {", ".join(self.products)}\nОбщее "
                f"количество категорй: {self.total_categories}\nОбщее количество уникальных "
                f"продуктов{self.total_unique_products}")
