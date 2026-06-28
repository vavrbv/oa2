from abc import ABC, abstractmethod


# Абстрактный класс,
# реализующий концепцию порта из гексагональной архитектуры.
class Port(ABC):
    # Все адаптеры, являющиеся классами-наследниками,
    # должны определить собственную реализацию метода do().
    @abstractmethod
    def do(self) -> None: ...


# Адаптер A - конкретная реализация порта.
class AdapterA(Port):
    def do(self) -> None:
        print("AdapterA")


# Адаптер B - конкретная реализация порта.
class AdapterB(Port):
    def do(self) -> None:
        print("AdapterB")


# На этапе исполнения программы, при вызове этой функции
# происходит подстановка конкретного класса (типа), реализующего заданный
# интерфейс.
def do(adapter: Port) -> None:
    adapter.do()


a = AdapterA()
b = AdapterB()

do(a)
do(b)
