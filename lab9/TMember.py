from __future__ import annotations

class TMember:
    
    def __init__(self, coeff: int = 0, degree: int = 0):
        if degree < 0: raise ValueError("degree must be non-negative")
        
        self.__coeff = coeff
        self.__degree = 0 if coeff == 0 else degree


    def read_degree(self) -> int:
        return self.__degree
    
    def write_degree(self, degree: int) -> None:
        self.__degree = degree

    def read_coeff(self) -> int:
        return self.__coeff
    
    def write_coeff(self, coeff: int) -> None:
        self.__coeff = coeff

    def is_equal(self, other: TMember) -> bool:
        return (self.__coeff == other.__coeff 
                and self.__degree == other.__degree)
    
    def differentiate(self) -> TMember:
        if (self.__degree == 0): return TMember(0, 0)

        else: return TMember(self.__coeff * self.__degree, self.__degree - 1)

    def compute(self, x) -> float:
        try:
            result =  self.coeff * (x ** self.power)
        except OverflowError:
            raise OverflowError("Overflow")
        
        return result
    
    def __str__(self) -> str:
        if self.power == 0:
            return f"{self.coeff}"
        elif self.power == 1:
            if self.coeff == 1:
                return "x"
            elif self.coeff == -1:
                return "-x"
            else:
                return f"{self.coeff}x"
        else:
            if self.coeff == 1:
                return f"x^{self.power}"
            elif self.coeff == -1:
                return f"-x^{self.power}"
            else:
                return f"{self.coeff}x^{self.power}"

    pass