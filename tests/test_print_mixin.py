from src.product import Product


def test_print_mixin(capsys):
    Product(name="Pineapple", description="Страна-поставщик Коста-Рика", price=460, quantity=10)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Pineapple', 'Страна-поставщик Коста-Рика', 460, 10)"
