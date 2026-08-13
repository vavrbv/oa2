from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class AbstractCollection(ABC, Generic[T]):
    @abstractmethod
    def add(self, value: T) -> None: ...


# Пример наследования с конкретизацией.
# AbstractCollection является абстрактным классом,
# задающим некоторый интерфейс, класс Collection
# предоставляет реализацию этого интерфейса.
class Collection(AbstractCollection, Generic[T]):
    def __init__(self) -> None:
        self._list: list[T]= []

    def add(self, value: T) -> None:
        self._list.append(value)


# Пример наследования вариаций.
# Класс Set переопределяет конструктор и метод add
# новой логикой, но оставляет сигнатуру нетронутой.
class Set(Collection, Generic[T]):
    def __init__(self) -> None:
        self._set: set[T] = set()

    def add(self, value: T) -> None:
        if value not in self._set:
            self._set.add(value)


class DoSomethingMixin:
    def do_something(self) -> None: ...


# Пример структурного наследования.
# Класс A наследуется от класса DoSomethingMixin
# и получает интерфейс и реализацию метода do_something,
# далее объекты класса A могут быть использованы полиморфно
# вместо объектов класса DoSomethingMixin.
class A(DoSomethingMixin):
    def a(self) -> None: ...
