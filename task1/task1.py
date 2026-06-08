from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


# Пример параметрического полиморфизма:
# один и тот же код вызывается для любого типа T
def polymorph_print(value: T) -> None:
    print(value)


class A:
    def print(self) -> None:
        print("a")


# Пример наследования: класс B наследуется от класса A
# и переопределяет метод print()
class B(A):
    def print(self) -> None:
        print("b")


# Пример полиморфизма подтипов:
# функция будет работать с базовым классом A
# и со всеми его потомками одинаковым образом
def subtype_print(value: A) -> None:
    value.print()


class C:
    def __init__(self, value: int = 42) -> None:
        self.value = value

    # Пример ad-hoc полиморфизма перегрузки оператора:
    # объекты класса C могут участвовать в сложении
    # как с другими объектами класса C, так и с целыми числами (объектами класса int).
    # В коде вызов будет выглядеть одинаково: C(...) + C(...),  C(...) + int(...)
    def __add__(self, other: object) -> C:
        if isinstance(other, C):
            return C(self.value + other.value)

        if isinstance(other, int):
            return C(self.value + other)

        raise NotImplementedError


class D:
    def print(self) -> None:
        print("d")


# Пример композиции: объект класса E содержит объект класса D
class E:
    def __init__(self) -> None:
        self.d = D()

    def print(self) -> None:
        self.d.print()
