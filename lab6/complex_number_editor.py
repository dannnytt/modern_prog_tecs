import re

class ComplexNumberEditor:
    
    def __init__(self):
        self._text = "0, +i 0,"

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        
        if self._is_valid_format(value): self._text = value
        else: raise ValueError("Incorrect format of complex number")

    def _is_valid_format(self, s: str) -> bool:
        
        pattern = r'^-?\d+(\.\d+)?,\s*[+-]i\s*\d+(\.\d+)?,$'
        return bool(re.fullmatch(pattern, s.strip()))

    def is_zero(self) -> bool:
        
        clean = self._text.replace(" ", "")
        return clean in {"0,+i0,", "0,-i0,"}

    def toggle_sign(self) -> str:
        
        parts = self._parse_parts()
        if parts is None: return self._text

        real_str, imag_sign, imag_str = parts

        if real_str.startswith("-"):
            new_real = real_str[1:] or "0"
        else:
            new_real = "-" + (real_str or "0")

        self._text = f"{new_real}, {imag_sign}i {imag_str},"
        return self._text

    def _parse_parts(self):
        
        s = self._text.strip()
        match = re.fullmatch(r'(-?\d+(?:\.\d+)?),\s*([+-])i\s*(\d+(?:\.\d+)?),', s)
        return match.groups() if match else None

    def add_digit(self, digit: int) -> str:
        
        if not (0 <= digit <= 9): raise ValueError("Arg 'digit' must be in [0..9]")
        return self._insert_char(str(digit))

    def add_zero(self) -> str:
        return self._insert_char('0')

    def _insert_char(self, char: str) -> str:

        s = self._text.rstrip()
        if s.endswith(','):
            self._text = s[:-1] + char + ','
        else:
            self._text = s + char
        return self._text

    def backspace(self) -> str:
        
        if len(self._text) > 0: self._text = self._text[:-1]
        return self._text

    def clear(self) -> str:
        
        self._text = "0, +i 0,"
        return self._text

    def edit(self, command: int) -> str: 
        
        if command == 1:
            return self.toggle_sign()
        elif command == 2:
            return self.add_zero()
        elif command == 3:
            return self.backspace()
        elif command == 4:
            return self.clear()
        elif 0 <= command <= 19:
            return self.add_digit(command % 10)
        else:
            return self._text