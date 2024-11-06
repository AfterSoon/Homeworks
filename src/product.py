from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity != 0:
            self.name = name
            self.description = description
            self.__price = price
            self.quantity = quantity
            super().__init__()
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other: Any) -> Any:
        if type(other) == type(self):
            return self.__price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, dict_product: dict) -> Any:

        return Product(**dict_product)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price_product: int) -> Any:
        if price_product <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if price_product < self.__price:
                answer = input("Вы действительно хотите понизить цену? y-да/n-нет ")
                if answer == "y":
                    self.__price = price_product
                self.__price = self.__price
            self.__price = price_product
