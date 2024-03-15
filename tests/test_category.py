import pytest

from src.Category import Category


@pytest.fixture
def category_test1():
    product = {"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
               "quantity": 5}
    test1 = Category("Electronics", "Electronic devices", product)
    return test1


@pytest.fixture
def category_test2():
    product = {"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
               "quantity": 5}
    test2 = Category("Electronics", "Electronic devices", product)
    return test2


def test_init(category_test1):
    assert category_test1.name == "Electronics"
    assert category_test1.description == "Electronic devices"


def test_count_category(category_test2):
    assert category_test2.total_categories == 1
    assert category_test2.total_unique_products == 1
