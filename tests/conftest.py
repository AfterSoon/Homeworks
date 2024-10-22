import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def apple():
    return Product(name="Green apple", description="Сезонные 2024 года", price=115.20, quantity=30)


@pytest.fixture
def pineapple():
    return Product(name="Pineapple", description="Страна-поставщик Коста-Рика", price=460, quantity=10)


@pytest.fixture
def category_fruit(apple, pineapple):
    return Category(name="Fruits", description="Сбор урожая - 2024", products=[apple, pineapple])
