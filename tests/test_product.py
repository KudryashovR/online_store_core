import pytest

from src.product import Product

@pytest.fixture
def product_test():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180_000.0,
                   5)


def test_init(product_test):
    assert product_test.name == "Samsung Galaxy C23 Ultra"
    assert product_test.description == "256GB, Серый цвет, 200MP камера"
    assert product_test.price == 180_000.0
    assert product_test.stock_quantity == 5
