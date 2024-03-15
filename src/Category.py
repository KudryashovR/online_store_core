class Category:
    name: str
    description: str
    products: list

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description

        if products:
            self.products = products
        else:
            self.products = []

    def __repr__(self):
        return f"{self.name} {self.description} {" ".join(self.products)}"
