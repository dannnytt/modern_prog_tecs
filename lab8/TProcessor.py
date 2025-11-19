from enum import Enum

class Operations(Enum):
    NONE = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

class Functions(Enum):
    REVERSE = 0
    SQUARE = 1

class TProcessor:
    
    def __init__(self, object1=None, object2=None):
        self._lop_res = object1 if object1 is not None else 0
        self._rop = object2 if object2 is not None else 0
        self._operation = Operations.NONE

    def reset_processor(self):
        self._lop_res = 0
        self._rop = 0
        self._operation = Operations.NONE

    def reset_operation(self):
        self._operation = Operations.NONE

    def execute_operation(self):
        match self._operation:
            case Operations.ADD:
                self._lop_res += self._rop
            
            case Operations.SUB:
                self._lop_res -= self._rop
            
            case Operations.MUL:
                self._lop_res *= self._rop
            
            case Operations.DIV:
                if self._rop == 0: 
                    raise ZeroDivisionError("Division by zero")
                self._lop_res /= self._rop

    def execute_function(self, function):
        match function:
            case Functions.REVERSE:
                self._rop = int(str(self._rop)[::-1])
                
            case Functions.SQUARE:
                self._rop = self._rop ** 2

    @property
    def lop(self):
        return self._lop_res

    @lop.setter
    def lop(self, value):
        self._lop_res = value

    @property
    def rop(self):
        return self._rop

    @rop.setter
    def rop(self, value):
        self._rop = value

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value

