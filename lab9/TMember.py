# TMember.py
from __future__ import annotations

class TMember:
    def __init__(self, coeff: int = 0, degree: int = 0):
        if degree < 0:
            raise ValueError("degree must be non-negative")
        # Храним данные в приватных полях
        self.__coeff = coeff
        self.__degree = 0 if coeff == 0 else degree

    # ---- snake_case API ----
    def read_coeff(self) -> int:
        return self.__coeff

    def write_coeff(self, coeff: int) -> None:
        self.__coeff = coeff
        # если coeff стал 0, степень в спецификации считается 0
        if coeff == 0:
            self.__degree = 0

    def read_degree(self) -> int:
        return self.__degree

    def write_degree(self, degree: int) -> None:
        if degree < 0:
            raise ValueError("degree must be non-negative")
        # если коэффициент 0, оставляем степень = 0
        if self.__coeff == 0:
            self.__degree = 0
        else:
            self.__degree = degree

    def is_equal(self, other: "TMember") -> bool:
        return (self.__coeff == other.__coeff and self.__degree == other.__degree)

    def differentiate(self) -> "TMember":
        # производная константы = 0
        if self.__degree == 0:
            return TMember(0, 0)
        return TMember(self.__coeff * self.__degree, self.__degree - 1)

    def compute(self, x) -> float:
        # Возвращаем float, чтобы соответствовать спецификации
        try:
            return float(self.coeff * (x ** self.power))
        except OverflowError:
            raise OverflowError("Overflow")

    def __str__(self) -> str:
        # Используем свойства coeff/power для удобства
        c = self.coeff
        p = self.power
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

    # ---- optional compatibility: camelCase ----
    # (нужны только если где-то ещё в проекте используются camelCase-имена)
    def readCoeff(self) -> int:
        return self.read_coeff()

    def writeCoeff(self, coeff: int) -> None:
        return self.write_coeff(coeff)

    def readPower(self) -> int:
        return self.read_degree()

    def writePower(self, degree: int) -> None:
        return self.write_degree(degree)

    # ---- properties для удобного доступа внутри класса/внешнего кода ----
    @property
    def coeff(self) -> int:
        return self.__coeff

    @property
    def power(self) -> int:
        return self.__degree
