from src.product import Product
from src.exceptions import AddZeroQuantityException


class Order:
    prod: 'Product'
    buying_quantity: int

    def __init__(self, prod: 'Product', buying_quantity: int) -> None:
        self.prod = prod
        if buying_quantity == 0:
            raise AddZeroQuantityException()
        else:
            self.buying_quantity = buying_quantity

    def get_total_price(self) -> float:
        return self.buying_quantity * self.prod.price

    def is_can_buy(self) -> bool:
        return self.buying_quantity < self.prod.stock_quantity

    def __str__(self) -> str:
        if self.is_can_buy():
            return (f"Закупаемый товар: {self.prod}\n"
                    f"Закупаемое количество: {self.buying_quantity}\n"
                    f"Итоговая цена: {self.get_total_price()}")
        else:
            return "Такого количества товара нет на складе"
