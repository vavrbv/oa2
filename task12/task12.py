from __future__ import annotations
from typing import Type, Any as AnyType
from copy import deepcopy


class General(object):
    # Операция копирования другого объекта в текущий.
    # Так как General не имеет конкретной реализации
    # полей, то копировать нечего.
    def copy_from(self, other: General) -> None: ...

    # Операция клонирования объекта.
    # Осуществляет глубокое копирование.
    def clone(self) -> General:
        return deepcopy(self)

    # Операция проверки равенства двух объектов.
    # Здесь равным будет считаться только объект сам себе,
    # то есть аналог self is other.
    def equal(self, other: General) -> bool:
        return self == other

    # Операция сериализации в строковый тип.
    def to_string(self) -> str:
        return str(self)

    # Операция десереализации из строкового типа.
    # Так как General не имеет конкретной реализации
    # полей, то из строки нельзя получить структуру объекта.
    def from_string(self, string: str) -> None: ...

    # Операция печати.
    def print(self) -> None:
        print(self)

    # Операция проверки соответствия типа.
    def is_type(self, concrete_type: Type) -> bool:
        return isinstance(self, concrete_type)

    # Операция получения типа текущего объекта.
    def type(self) -> Type:
        return type(self)

    # Операция попытки присваивания
    def assignment_attempt(self, source: AnyType) -> None:
        # Если тип текущего объекта соответствует типу
        # объекта source или является его надтипом,
        # то данные этого объекта можно скопировать в текущий.
        if isinstance(source, self.type()):
            self.copy_from(source)
        else:
            self.copy_from(VOID)


class Any(General): ...

# Замыкание собственным типом None через множественное наследование
# от типов Any и General
class CustomNone(Any, General): ...


VOID = CustomNone()

a = General()
a1 = General()
b = Any()
b1 = Any()
c = 5

a.assignment_attempt(a1)
a.assignment_attempt(b)
a.assignment_attempt(c)

b.assignment_attempt(b1)
b.assignment_attempt(a)
b.assignment_attempt(c)
