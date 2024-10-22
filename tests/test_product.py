def test_product_init(apple, pineapple):
    assert apple.name == "Green apple"
    assert apple.description == "Сезонные 2024 года"
    assert apple.price == 115.20
    assert apple.quantity == 30

    assert pineapple.name == "Pineapple"
    assert pineapple.description == "Страна-поставщик Коста-Рика"
    assert pineapple.price == 460
    assert pineapple.quantity == 10
