# В Python допустимы только варианты 1 и 4, так как видимость
# метода привязана к его имени, то изменить её нельзя без изменения
# имени, что будет являться другим методом. 

# Пример варианта 1
class A:
    def print(self) -> None:
        print("a")


class B(A):
    def print(self) -> None:
        print("b")

    # print() и _print() - разные методы
    def _print(self) -> None:
        print("another b")


# Пример варианта 4
class C:
    def _print(self) -> None:
        print("c")


class D(C):
    def _print(self) -> None:
        print("d")

    # _print() и print() - разные методы
    def print(self) -> None:
        print("another d")


b = B()
d = D()

b.print()
b._print()

d._print()
d.print()
