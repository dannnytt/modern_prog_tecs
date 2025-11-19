import unittest
from typing import List

from src.operations import Operations

class TestOperations(unittest.TestCase):
    
    """ Тесты для метода Operations.get_max """
    def test_max_first_param_is_greater(self):
        self.assertEqual(Operations.get_max(3, 2, 1), 3)

    """ Тесты для метода Operations.get_reverse_even_digits """
    def test_get_reverse_even_digits_with_negative_number(self):
        self.assertEqual(Operations.get_reverse_even_digits(-1256), 62)
    
    def test_get_reverse_even_digits_having_even_digits(self):
        self.assertEqual(Operations.get_reverse_even_digits(124356), 642)

    def test_get_reverse_even_digits_not_having_even_digits(self):
        self.assertEqual(Operations.get_reverse_even_digits(1357), 0)
    
    def test_get_reverse_even_digits_with_zero(self):
        self.assertEqual(Operations.get_reverse_even_digits(0), 0)

    """ Тесты для метода Operations.get_min_digit"""
    def test_get_min_digit_with_negative_number(self):
        self.assertEqual(Operations.get_min_digit(-34165), 1)

    def test_get_min_digit_with_positive_number(self):
        self.assertEqual(Operations.get_min_digit(34265), 2)

    def test_get_min_digit_single_digit(self):
        self.assertEqual(Operations.get_min_digit(7), 7)

    def test_get_min_digit_with_zero(self):
        self.assertEqual(Operations.get_min_digit(0), 0)


    """ Тесты для метода Operations.get_sum_below_main_diagonal """
    def test_get_sum_odd_below_main_diagonal_with_correct_param(self):
        matrix = [[1, 2, 4], [3, 5, 6], [7, 8, 9]]
        self.assertEqual(Operations.get_sum_odd_below_main_diagonal(matrix), 10)

    def test_get_sum_odd_with_no_odd_numbers(self):
        matrix = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        self.assertEqual(Operations.get_sum_odd_below_main_diagonal(matrix), 0)

    def test_get_sum_odd_with_1x1_matrix(self):
        self.assertEqual(Operations.get_sum_odd_below_main_diagonal([[5]]), 0)

    def test_get_sum_odd_below_main_diagonal_with_multiple_odd_numbers(self):
        matrix = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
        self.assertEqual(Operations.get_sum_odd_below_main_diagonal(matrix), 14)

if __name__ == "__main__":
    unittest.main()