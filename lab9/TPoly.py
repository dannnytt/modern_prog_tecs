from __future__ import annotations

from typing import Dict
from TMember import TMember

class TPoly:
    # создание полинома
    def __init__(self, coeff: int = 0, degree: int = 0) -> None:
        if coeff == 0:
            self.polynom: Dict[int, TMember] = {}       # ключ - степень; значение - TMember
        else:
            self.polynom = {degree: TMember(coeff, degree)}

    def max_degree(self) -> int:
        if not self.polynom:
            return 0    # cтепень нулевого полинома
        return max(self.polynom.keys())

    def coeff(self, degree: int) -> int:
        return self.polynom.get(degree, TMember()).read_coeff() # коэффициент при заданной степени

    def clear(self):
        self.polynom.clear()

    def __add__(self, other: TPoly) -> TPoly:
        result = TPoly()
        result.polynom = self.polynom.copy()
        for deg, mon in other.polynom.items():
            if deg in result.polynom:
                new_coeff = result.polynom[deg].read_coeff() + mon.read_coeff()
                if new_coeff != 0:
                    result.polynom[deg] = TMember(new_coeff, deg)
                else:
                    del result.polynom[deg]
            else:
                result.polynom[deg] = mon
        return result

    def __sub__(self, other: TPoly) -> TPoly:
        result = TPoly()
        result.polynom = self.polynom.copy()
        for deg, mon in other.polynom.items():
            if deg in result.polynom:
                new_coeff = result.polynom[deg].read_coeff() - mon.read_coeff()
                if new_coeff != 0:
                    result.polynom[deg] = TMember(new_coeff, deg)
                else:
                    del result.polynom[deg]
            else:
                result.polynom[deg] = TMember(-mon.read_coeff(), deg)
        return result

    def minus(self) -> TPoly:
        result = TPoly()
        for deg, mon in self.polynom.items():
            result.polynom[deg] = TMember(-mon.read_coeff(), deg)
        return result

    def __mul__(self, other: TPoly) -> TPoly:
        result = TPoly()
        for deg1, mon1 in self.polynom.items():
            for deg2, mon2 in other.polynom.items():
                new_deg = deg1 + deg2
                new_coeff = mon1.read_coeff() * mon2.read_coeff()
                if new_deg in result.polynom:
                    old_coeff = result.polynom[new_deg].read_coeff()
                    total_coeff = old_coeff + new_coeff
                    if total_coeff != 0:
                        result.polynom[new_deg] = TMember(total_coeff, new_deg)
                    else:
                        del result.polynom[new_deg]
                else:
                    if new_coeff != 0:
                        result.polynom[new_deg] = TMember(new_coeff, new_deg)
        return result

    def differentiate(self) -> TPoly:
        result = TPoly()
        for deg, mon in self.polynom.items():
            diff_mon = mon.differentiate()
            if diff_mon.read_coeff() != 0:
                result.polynom[diff_mon.read_degree()] = diff_mon
        return result

    def compute(self, x: float) -> float:
        if x == 0:
            return float(self.coeff(0))
        
        total = 0.0
        for mon in self.polynom.values():
            total += mon.compute(x)
        return total

    def elem(self, pos: int) -> TMember:
        if pos < 0 or pos >= len(self.polynom):
            return TMember()
        
        sorted_items = sorted(self.polynom.items(), key=lambda item: item[0], reverse=True)
        return sorted_items[pos][1]

    def __getitem__(self, pos: int) -> TMember:
        return self.elem(pos)

    def __repr__(self):
        if not self.polynom:
            return "0"
        
        terms = []
        for deg in sorted(self.polynom.keys(), reverse=True):
            term = self.polynom[deg]
            terms.append(str(term))
        return " + ".join(terms).replace("+ -", "- ")
    
    def normalize(self) -> None:
        zeros = [deg for deg, m in list(self.polynom.items()) if m.read_coeff() == 0]
        for deg in zeros:
            del self.polynom[deg]   # удалены все степени, у которых коэффициент равен нулю

        combined = {}
        for deg, m in self.polynom.items(): # собирает все одночлены одинаковой степени в новый словарь
            if deg in combined:
                combined[deg] = TMember(combined[deg].read_coeff() + m.read_coeff(), deg)
            else:
                combined[deg] = TMember(m.read_coeff(), deg)
        self.polynom = {deg: m for deg, m in combined.items() if m.read_coeff() != 0}

