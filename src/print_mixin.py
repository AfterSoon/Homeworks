from typing import Any


class PrintMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(repr(self))

    def __repr__(self) -> Any:
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
