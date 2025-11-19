import random
from typing import List

from src.operations import Operations

if __name__ == "__main__":
    
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    c = random.randint(0, 1000)
    print(f"max({a}, {b}, {c}) = {Operations.get_max(a, b, c)}")
    print()

    number= random.randint(0, 100000)
    print(f"number = {number},  reversed_even_digits = {Operations.get_reverse_even_digits(number)}")
    print()

    print(f"number = {number},  min_digit = {Operations.get_min_digit(number)}")
    print()

    rows = 3
    cols = 3
    matrix = [[random.randint(0, 1000) for _ in range(cols)] for _ in range(rows)]

    print(f"matrix = {matrix}")
    print(f"sum of odd elems below main diagonal = {Operations.get_sum_odd_below_main_diagonal(matrix)}")
