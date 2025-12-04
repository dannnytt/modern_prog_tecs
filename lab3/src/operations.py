from typing import List

class Operations:
    
    @staticmethod
    def get_max(num1: int, num2: int, num3: int) -> int:
        
        max: int = num1
        if (num2 >= max): 
            max = num2
        if (num3 >= max): 
            max = num3

        return max
    
    @staticmethod
    def get_reverse_even_digits(number: int) -> int :

        result: int = 0
        number = abs(number)

        while (number > 0):
            digit: int = number % 10

            if (digit % 2 == 0):
                result *= 10
                result += digit
            number //= 10

        return result
    
    @staticmethod
    def get_min_digit(number: int) -> int:

        number = abs(number)
        
        min_digit: int = number % 10
        number //= 10

        while (number > 0):
            digit = number % 10
            
            if (digit < min_digit):
                min_digit = digit
            number //= 10

        return min_digit
    
    @staticmethod
    def get_sum_odd_below_main_diagonal(matrix: List[List[int]]) -> int:
        
        sum_val = 0
        size = len(matrix)
        for i in range(size):
            for j in range(i):
                if matrix[i][j] % 2 != 0:
                    sum_val += matrix[i][j]
        
        return sum_val
