from __future__ import annotations
from typing import Type
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


class Any(General): ...

# Замыкание собственным типом None через множественное наследование
# от типов Any и None
class CustomNone(Any, General): ...


VOID = CustomNone()


# Функция вывода информации об объекте работает для всех подтипов General
def print_info(custom_object: General) -> None:
    print(
        "Object: {}, type: {}".format(custom_object.to_string(), custom_object.type()),
    )


general_object = General()
any_object = Any()

print_info(general_object)
print_info(any_object)
# Так как CustomNone является подтипом General, то функция print_info
# корректно обрабатывает объект VOID
print_info(VOID)
