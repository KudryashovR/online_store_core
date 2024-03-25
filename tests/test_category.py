import pytest
from unittest.mock import Mock

from src.category import Category


@pytest.fixture
def manual_category():
    return Category('Empty Category', 'This is an empty category', {"name": "Product",
                                                                    "description": "Test product", "price": 10.99,
                                                                    "quantity": 100})


@pytest.fixture
def empty_category():
    return Category('Empty Category', 'This is an empty category')


@pytest.fixture
def filled_category():
    product_mock = Mock(name='Product', description='Test product', price=10.99, stock_quantity=100)

    return Category('Filled Category', 'This category has one product',
                    prod={"name": product_mock.name, "description": product_mock.description,
                          "price": product_mock.price, "quantity": product_mock.stock_quantity})


@pytest.fixture
def sample_product():
    return Mock(name='Product', description='Test product', price=10.99, stock_quantity=100)


@pytest.fixture
def another_sample_product():
    return Mock(name='AnotherProduct', description='Another test product', price=15.99, stock_quantity=50)


@pytest.fixture
def category():
    return Category('Test Category', 'A category for testing')


def test_category_constructor(empty_category):
    assert empty_category.name == 'Empty Category'
    assert empty_category.description == 'This is an empty category'
    assert len(empty_category.prod) == 0


def test_add_prod(empty_category):
    product_mock = Mock(name='Product', description='Test product', price=10.99, stock_quantity=100)
    empty_category.add_prod(product_mock)

    assert len(empty_category.prod) == 1
    assert empty_category.prod[0] == product_mock


def test_str(empty_category):
    expected_str = "Empty Category, количество продуктов: 0 шт."

    assert str(empty_category) == expected_str


def test_len_on_empty_category(empty_category):
    assert len(empty_category) == 0


def test_len_on_filled_category(filled_category):
    assert len(filled_category) == 100


def test_prod_property(empty_category, filled_category):
    assert isinstance(empty_category.prod, list)
    assert len(empty_category.prod) == 0
    assert len(filled_category.prod) == 1


def test_repr(empty_category):
    expected_repr = ('Category(Empty Category, This is an empty category, [])\n'
                     'total_categories: 1\n'
                     'total_unique_products: 0')

    assert repr(empty_category) == expected_repr


def test_add_prod_success(category, sample_product):
    category.add_prod(sample_product)

    assert len(category.prod) == 1
    assert category.total_unique_products == 1
    assert category.prod[0] == sample_product


def test_add_prod_different_type_raises_error(category, sample_product, another_sample_product):
    category.add_prod(sample_product)

    with pytest.raises(ValueError):
        category.add_prod(another_sample_product)


def test_add_multiple_products(category, sample_product):
    for _ in range(5):
        category.add_prod(sample_product)

    assert len(category.prod) == 5
    assert category.total_unique_products == 5


def test_product(manual_category):
    expected_product = "Product, 10.99 руб. Остаток: 100 шт."

    assert manual_category.product == expected_product
