"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture()
def cart():
    return Cart()


@pytest.fixture
def beer():
    return Product("Miller", 100, "This is a Miller", 1000)


@pytest.fixture()
def phone():
    return Product("Samsung", 13456, "Samsung A333", 1)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, beer):
        assert beer.check_quantity(1000) is True
        assert beer.check_quantity(1001) is False

    def test_product_buy(self, beer):
        beer.buy(99)
        assert beer.quantity == 901

    def test_product_buy_more_than_available(self, beer):
        with pytest.raises(ValueError):
            beer.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, beer, cart):
        cart.add_product(beer, 12)
        assert cart.products[beer] == 12

        cart.add_product(beer, 2)
        assert cart.products[beer] == 14

    def test_add_product_without_count(self, beer, cart):
        cart.add_product(beer)
        assert cart.products[beer] == 1

    def test_remove_product(self, beer, cart):
        cart.add_product(beer, 12)
        cart.remove_product(beer, 12)
        assert cart.products == {beer: 0}

    def test_remove_product_with_less_count(self, beer, cart):
        cart.add_product(beer, 12)
        cart.remove_product(beer, 11)
        assert cart.products == {beer: 1}

    def test_remove_product_with_more_count(self, beer, cart):
        cart.add_product(beer, 12)
        cart.remove_product(beer, 13)
        assert cart.products == {}

    def test_remove_product_without_count(self, beer, cart):
        cart.add_product(beer, 12)
        cart.remove_product(beer)
        assert cart.products == {}

    def test_clear_basket(self, beer, cart, phone):
        cart.add_product(beer, 12)
        cart.add_product(phone, 1)
        cart.clear()

        assert cart.products == {}

    def test_total_price(self, beer, cart, phone):
        cart.add_product(beer, 12)
        cart.add_product(phone, 1)

        assert cart.get_total_price() == 14656

    def test_buy(self, cart, beer, phone):
        cart.add_product(beer, 12)
        cart.add_product(phone, 1)

        cart.buy()

        assert beer.quantity == 988
        assert phone.quantity == 0

        cart.add_product(phone, 1)

        with pytest.raises(ValueError):
            assert cart.buy() is ValueError
