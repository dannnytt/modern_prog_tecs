from __future__ import annotations
from typing import Tuple

class TMember:
    def __init__(self, coeff: int = 0, degree: int = 0):
        if degree < 0:
            raise ValueError("degree must be non-negative")
        self.__coeff = int(coeff)
        # если coeff == 0, степень нормализуем в 0
        self.__degree = 0 if self.__coeff == 0 else int(degree)
        self.normalize()

    def normalize(self) -> None:
        if self.__coeff == 0:
            self.__degree = 0
        if self.__degree < 0:
            raise ValueError("degree must be non-negative")

    def as_tuple(self) -> Tuple[int, int]:
        """Возвращает (degree, coeff). Удобно для агрегации/сортировки."""
        return (self.__degree, self.__coeff)

    def read_coeff(self) -> int:
        return self.__coeff

    def write_coeff(self, coeff: int) -> None:
        self.__coeff = int(coeff)
        # при записи нуля — степень должна быть 0 по спецификации
        if self.__coeff == 0:
            self.__degree = 0
        self.normalize()

    def read_degree(self) -> int:
        return self.__degree

    def write_degree(self, degree: int) -> None:
        if degree < 0:
            raise ValueError("degree must be non-negative")
        # если коэффициент = 0 — сохраняем степень 0
        if self.__coeff == 0:
            self.__degree = 0
        else:
            self.__degree = int(degree)
        self.normalize()

    @property
    def coeff(self) -> int:
        return self.__coeff

    @property
    def power(self) -> int:
        return self.__degree

    def readCoeff(self) -> int:
        return self.read_coeff()

    def writeCoeff(self, coeff: int) -> None:
        return self.write_coeff(coeff)

    def readPower(self) -> int:
        return self.read_degree()

    def writePower(self, degree: int) -> None:
        return self.write_degree(degree)

    def is_equal(self, other: "TMember") -> bool:
        return isinstance(other, TMember) and (self.__coeff == other.__coeff and self.__degree == other.__degree)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TMember):
            return False
        return self.is_equal(other)

    def __add__(self, other: "TMember") -> "TMember":
        if not isinstance(other, TMember):
            return NotImplemented
        if self.__degree != other.__degree:
            return NotImplemented
        return TMember(self.__coeff + other.__coeff, self.__degree)

    def __iadd__(self, other: "TMember") -> "TMember":
        if not isinstance(other, TMember):
            raise TypeError("Can only add TMember")
        if self.__degree != other.__degree:
            raise ValueError("Cannot add members with different degrees")
        self.__coeff += other.__coeff
        self.normalize()
        return self

    def __sub__(self, other: "TMember") -> "TMember":
        if not isinstance(other, TMember):
            return NotImplemented
        if self.__degree != other.__degree:
            return NotImplemented
        return TMember(self.__coeff - other.__coeff, self.__degree)

    def __isub__(self, other: "TMember") -> "TMember":
        if not isinstance(other, TMember):
            raise TypeError("Can only subtract TMember")
        if self.__degree != other.__degree:
            raise ValueError("Cannot subtract members with different degrees")
        self.__coeff -= other.__coeff
        self.normalize()
        return self

    def __mul__(self, other: "TMember") -> "TMember":
        if not isinstance(other, TMember):
            return NotImplemented
        return TMember(self.__coeff * other.__coeff, self.__degree + other.__degree)

    def __imul__(self, other: "TMember") -> "TMember":
        if not isinstance(other, TMember):
            raise TypeError("Can only multiply by TMember")
        self.__coeff *= other.__coeff
        self.__degree += other.__degree
        self.normalize()
        return self

    def __neg__(self) -> "TMember":
        return TMember(-self.__coeff, self.__degree)

    def differentiate(self) -> "TMember":
        if self.__degree == 0:
            return TMember(0, 0)
        return TMember(self.__coeff * self.__degree, self.__degree - 1)

    def compute(self, x) -> float:
        try:
            return float(self.__coeff * (x ** self.__degree))
        except OverflowError:
            raise OverflowError("Overflow")

    def __str__(self) -> str:
        c = self.__coeff
        p = self.__degree
        if p == 0:
            return f"{c}"
        elif p == 1:
            if c == 1:
                return "x"
            elif c == -1:
                return "-x"
            else:
                return f"{c}x"
        else:
            if c == 1:
                return f"x^{p}"
            elif c == -1:
                return f"-x^{p}"
            else:
                return f"{c}x^{p}"

    def __repr__(self) -> str:
        return f"TMember({self.__coeff}, {self.__degree})"
