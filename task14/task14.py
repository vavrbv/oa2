from __future__ import annotations

import copy


class General: ...


class Any(General):
    # Так как тип любого подтипа этой системы типов
    # является подтипом Any, то, при определении сложения
    # в Any возможны ситуации сложения объектов,
    # которые невозможно сложить друг с другом.
    # В таком случае результат сложения любых Any объектов
    # определяется как VOID.
    def __add__(self, other: object) -> Any:
        return VOID


class Void(Any): ...


class Vector[T](Any):
    def __init__(self, values: list[T]) -> None:
        self._values = values

    def __add__(self,  other: object) -> Any:
        if (
            isinstance(other, Vector)
            and self.size() == other.size()
        ):
            return Vector[T](
                [
                    value1 + value2
                    for value1, value2
                    in zip(self._values, other.values())
                ]
            )

        return VOID

    def size(self) -> int:
        return len(self._values)

    def values(self) -> list[T]:
        return copy.deepcopy(self._values)

    def __str__(self) -> str:
        return "[{}]".format(", ".join(str(value) for value in self._values))


class CustomInteger(Any):
    def __init__(self, value: int) -> None:
        self._value = value

    def __add__(self, other: object) -> Any:
        if isinstance(other, CustomInteger):
            return CustomInteger(self._value + other.value())

        return super().__add__(other)

    def value(self) -> int:
        return self._value

    def __str__(self) -> str:
        return str(self._value)


VOID = Void()


vector1 = Vector[CustomInteger]([CustomInteger(1), CustomInteger(2), CustomInteger(3)])
vector2 = Vector[CustomInteger]([CustomInteger(4), CustomInteger(5), CustomInteger(6)])

matrix1 = Vector[Vector[CustomInteger]](
    [
        Vector[CustomInteger](
            [CustomInteger(1), CustomInteger(2), CustomInteger(3)],
        ),
        Vector[CustomInteger](
            [CustomInteger(4), CustomInteger(5), CustomInteger(6)],
        ),
    ]
)
matrix2 = Vector[Vector[CustomInteger]](
    [
        Vector[CustomInteger](
            [CustomInteger(1), CustomInteger(2), CustomInteger(3)],
        ),
        Vector[CustomInteger](
            [CustomInteger(4), CustomInteger(5), CustomInteger(6)],
        ),
    ]
)

# Результат: [5, 7, 9]
print(vector1 + vector2)

# Результат: [[2, 4, 6], [8, 10, 11]]
print(matrix1 + matrix2)

# Результат: VOID
print(matrix1 + "abc")
