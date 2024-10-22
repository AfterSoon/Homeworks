from src.product import Product


def test_category_init(category_fruit, apple, pineapple):
    assert category_fruit.name == "Fruits"
    assert category_fruit.description == "Сбор урожая - 2024"
    assert category_fruit.products == [apple, pineapple]

    assert category_fruit.category_count == 1
    assert category_fruit.product_count == 2
