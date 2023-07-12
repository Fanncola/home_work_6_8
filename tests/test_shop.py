"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture()
def cart():
    return Cart()


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def phone():
    return Product("Samsung", 1, "Samsung A333", 13456)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        product.buy(99)
        assert product.quantity == 901

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, 12)

        assert cart.products[product] == 12

    def test_remove_product(self, product, cart):
        cart.add_product(product, 12)
        cart.remove_product(product, 13)

        assert cart.products == {}

    def test_clear_basket(self, product, cart, phone):
        cart.add_product(product, 12)
        cart.add_product(phone, 1)
        cart.clear()

        assert cart.products == {}

    def test_total_price(self, product, cart, phone):
        cart.add_product(product, 12)
        cart.add_product(phone, 1)
        cart.get_total_price()
