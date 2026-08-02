class A:
    def print(self) -> None:
        print("A")


class B(A):
    def print(self) -> None:
        print("B")


class C:
    # В качестве объекта obj могут выступать объекты классов A и B
    def polymorph_print(self, obj: A) -> None:
        obj.print()

    # Список объектов класса B, также может быть использован как obj_list
    def covariant_print(self, obj_list: list[A]) -> None:
        for obj in obj_list:
            obj.print()
