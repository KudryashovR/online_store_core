import pytest
from unittest.mock import patch

from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def prod1():
    return Product("Tea Kettle", "Stainless steel tea kettle", 120.50, 10)


@pytest.fixture
def prod2():
    return Product("Coffee Maker", "Drip coffee maker", 99.99, 5)


@pytest.fixture
def non_product():
    return Smartphone("Coffee Maker", "Drip coffee maker", 99.99, 5, "grey",
                      125, "Maker", 125)


def test_product_initialization():
    product = Product("Ноутбук", "Высокопроизводительный ноутбук", 100000, 50, "Черный")

    assert product.name == "Ноутбук"
    assert product.description == "Высокопроизводительный ноутбук"
    assert product.price == 100000
    assert product.stock_quantity == 50
    assert product.color == "Черный"


def test_product_representation():
    product = Product("Мышка", "Игровая мышь", 5000, 100, "Красный")

    assert str(product) == "Мышка, 5000 руб. Остаток: 100 шт."
    assert repr(product).startswith("Product(Мышка")


def test_product_addition():
    product1 = Product("Планшет", "Планшет для рисования", 20000, 30)
    product2 = Product("Клавиатура", "Механическая клавиатура", 7000, 40)
    total_price = product1 + product2

    assert total_price == (30 * 20000) + (40 * 7000)

    with pytest.raises(ValueError):
        product1 + "не продукт"


def test_create_product():
    prod_data = {"name": "Монитор", "description": "4K монитор", "price": 30000, "quantity": 20}
    product = Product.create_product(prod_data)

    assert product.name == "Монитор"
    assert product.description == "4K монитор"
    assert product.price == 30000
    assert product.stock_quantity == 20


def test_check_unique_items():
    products_list = [
        {"name": "Планшет", "price": 20000, "quantity": 30},
        {"name": "Планшет", "price": 22000, "quantity": 15},
        {"name": "Мышка", "price": 1500, "quantity": 50}
    ]
    unique_products = Product.check_unique_items(products_list)

    assert len(unique_products) == 2

    for product in unique_products:
        if product["name"] == "Планшет":
            assert product["price"] == 22000
            assert product["quantity"] == 45
        elif product["name"] == "Мышка":
            assert product["price"] == 1500
            assert product["quantity"] == 50


def test_change_price_with_input():
    product = Product("Планшет", "Планшет для рисования", 20000, 30)

    with patch('builtins.input', return_value='y'):
        product.price = 15000

        assert product.price == 15000


def test_smartphone_initialization():
    smartphone = Smartphone("Galaxy S21", "Высокопроизводительный смартфон", 80000,
                            25, "Черный", 125, "S21", 128)

    assert smartphone.name == "Galaxy S21"
    assert smartphone.description == "Высокопроизводительный смартфон"
    assert smartphone.price == 80000
    assert smartphone.stock_quantity == 25
    assert smartphone.efficiency == 125
    assert smartphone.model_name == "S21"
    assert smartphone.internal_memory == 128
    assert smartphone.color == "Черный"


def test_smartphone_create_product():
    prod_data = {
        "name": "Xiaomi Mi 11",
        "description": "Флагман с высоким разрешением экрана",
        "price": 60000,
        "quantity": 15,
        "efficiency": "Высокая",
        "model_name": "Mi 11",
        "internal_memory": 256,
        "color": "Синий"
    }
    smartphone = Smartphone.create_product(prod_data)

    assert smartphone.name == "Xiaomi Mi 11"
    assert smartphone.description == "Флагман с высоким разрешением экрана"
    assert smartphone.price == 60000
    assert smartphone.stock_quantity == 15
    assert smartphone.efficiency == "Высокая"
    assert smartphone.model_name == "Mi 11"
    assert smartphone.internal_memory == 256
    assert smartphone.color == "Синий"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass("Зеленый ковер", "Газонная трава для сада", 5000, 40,
                           "Зеленый", "Нидерланды", 14)

    assert lawn_grass.name == "Зеленый ковер"
    assert lawn_grass.description == "Газонная трава для сада"
    assert lawn_grass.price == 5000
    assert lawn_grass.stock_quantity == 40
    assert lawn_grass.origin_country == "Нидерланды"
    assert lawn_grass.germination_period == 14
    assert lawn_grass.color == "Зеленый"


def test_lawn_grass_create_product():
    prod_data = {
        "name": "Английский газон",
        "description": "Классический газон для вашего сада",
        "price": 4500,
        "quantity": 60,
        "origin_country": "Великобритания",
        "germination_period": "10 дней",
        "color": "Ярко-зеленый"
    }
    lawn_grass = LawnGrass.create_product(prod_data)

    assert lawn_grass.name == "Английский газон"
    assert lawn_grass.description == "Классический газон для вашего сада"
    assert lawn_grass.price == 4500
    assert lawn_grass.stock_quantity == 60
    assert lawn_grass.origin_country == "Великобритания"
    assert lawn_grass.germination_period == "10 дней"
    assert lawn_grass.color == "Ярко-зеленый"


def test_product_addition_same_type(prod1, prod2):
    total_value = prod1 + prod2
    expected_value = (prod1.stock_quantity * prod1.price + prod2.stock_quantity * prod2.price)

    assert total_value == expected_value


def test_product_addition_with_different_type(prod1, non_product):
    with pytest.raises(ValueError) as e:
        _ = prod1 + non_product

    assert "Типы складываемых объектов не совпадают" in str(e.value)


def test_product_addition_with_itself(prod1):
    total_value = prod1 + prod1
    expected_value = 2 * (prod1.stock_quantity * prod1.price)

    assert total_value == expected_value
