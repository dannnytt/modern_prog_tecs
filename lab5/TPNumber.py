from __future__ import annotations

class TPNumber:
    
    def __init__(self, a: float, b: int, c: int):
        if (b < 2 or b > 16): 
            raise ValueError("arg 'b' must be in [2..16].")
        
        if (c < 0): raise ValueError("arg 'c' must be >= 0.")

        self.__num = a
        self.__base = b
        self.__accuracy = c

    
    @classmethod
    def from_strings(cls, a: str, b: str, c: str):
        return cls(float(a), int(b), int(c))

    
    def copy(self) -> TPNumber:
        return TPNumber(self.__num, self.__base, self.__accuracy)

    
    def add(self, d: TPNumber) -> TPNumber:
        
        if (self.__base != d.__base): raise ValueError("'base' must be same.")
        accuracy = max(self.__accuracy, d.__accuracy)

        return TPNumber(self.__num + d.__num, self.__base, accuracy)

    
    def multiply(self, d: TPNumber) -> TPNumber:
        
        if (self.__base != d.__base): raise ValueError("'base must be same.'")
        accuracy = max(self.__accuracy, d.__accuracy)

        return TPNumber(self.__num * d.__num, self.__base, accuracy)
    
    
    def subtract(self, d: TPNumber) -> TPNumber:
        
        if (self.__base != d.__base): raise ValueError("'base must be same.'")
        accuracy = max(self.__accuracy, d.__accuracy)

        return TPNumber(self.__num - d.__num, self.__base, accuracy)


    def divide(self, d: TPNumber) -> TPNumber:
        
        if (d.__num == 0.0): raise ValueError("the field 'n' of the number 'd must not be 0.")
        if (self.__base != d.__base): raise ValueError("'base must be same.'")
        accuracy = max(self.__accuracy, d.__accuracy)

        return TPNumber(self.__num / d.__num, self.__base, accuracy)

    def reverse(d: TPNumber) -> TPNumber:
        if (d.__num == 0.0): raise ValueError("the field 'n' of the number 'd must not be 0.")
        
        return TPNumber(1 / d.__num, d.__base, d.__accuracy)
        

    def square(self) -> TPNumber:
        return TPNumber(self.__num ** 2, self.__base, self.__accuracy)
    
    @property
    def p_num(self) -> float:
        return self.__num
    
    @property
    def p_str(self) -> str:
        return str(self.__num)
    
    @property    
    def base_num(self) -> int:
        return self.__base
    
    @property
    def base_str(self) -> str:
        return str(self.__base)

    @property
    def accuracy_num(self) -> int:
        return self.__accuracy
    
    @property
    def accuracy_str(self) -> str:
        return str(self.__accuracy)

    