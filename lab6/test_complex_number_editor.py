import pytest
from complex_number_editor import ComplexNumberEditor


class TestComplexNumberEditorC2:

    # ---------- Тесты для __init__ ----------
    def test_initial_state_is_zero(self):
        editor = ComplexNumberEditor()
        assert editor.text == "0, +i 0,"
        assert editor.is_zero() is True

    # ---------- Тесты для is_zero() ----------
    def test_is_zero_true_cases(self):
        editor = ComplexNumberEditor()
        editor.text = "0, +i 0,"
        assert editor.is_zero() is True

        editor.text = "0, -i 0,"
        assert editor.is_zero() is True

    def test_is_zero_false_cases(self):
        editor = ComplexNumberEditor()
        editor.text = "1, +i 0,"
        assert editor.is_zero() is False

        editor.text = "0, +i 1,"
        assert editor.is_zero() is False

        editor.text = "-0, +i 0,"
        assert editor.is_zero() is False

    # ---------- Тесты для _is_valid_format() ----------
    def test_valid_format_positive(self):
        editor = ComplexNumberEditor()
        assert editor._is_valid_format("0, +i 0,") is True
        assert editor._is_valid_format("123, -i 45.67,") is True
        assert editor._is_valid_format("-5, +i 0.1,") is True

    def test_valid_format_negative(self):
        editor = ComplexNumberEditor()
        assert editor._is_valid_format("abc") is False
        assert editor._is_valid_format("1 + 2i") is False
        assert editor._is_valid_format("1, +i ,") is False
        assert editor._is_valid_format("1, i 2,") is False
        assert editor._is_valid_format("1.2.3, +i 4,") is False

    # ---------- Тесты для text.setter ----------
    def test_set_valid_text(self):
        editor = ComplexNumberEditor()
        editor.text = "5, -i 3.14,"
        assert editor.text == "5, -i 3.14,"

    def test_set_invalid_text_raises(self):
        editor = ComplexNumberEditor()
        with pytest.raises(ValueError):
            editor.text = "неправильная строка"

    # ---------- Тесты для toggle_sign() ----------
    def test_toggle_sign_positive_to_negative(self):
        editor = ComplexNumberEditor()
        editor.text = "123, +i 45,"
        editor.toggle_sign()
        assert editor.text == "-123, +i 45,"

    def test_toggle_sign_negative_to_positive(self):
        editor = ComplexNumberEditor()
        editor.text = "-42, -i 7,"
        editor.toggle_sign()
        assert editor.text == "42, -i 7,"

    def test_toggle_sign_on_zero(self):
        editor = ComplexNumberEditor()
        editor.text = "0, +i 0,"
        editor.toggle_sign()
        assert editor.text == "-0, +i 0,"

    def test_toggle_sign_on_invalid_format(self):
        editor = ComplexNumberEditor()
        editor._text = "некорректно"
        result = editor.toggle_sign()
        assert result == "некорректно"

    # ---------- Тесты для add_digit() ----------
    @pytest.mark.parametrize("digit", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_add_digit_valid(self, digit):
        editor = ComplexNumberEditor()
        editor.text = "1, +i 2,"
        result = editor.add_digit(digit)
        assert result == f"1, +i 2{digit},"

    def test_add_digit_invalid_raises(self):
        editor = ComplexNumberEditor()
        with pytest.raises(ValueError):
            editor.add_digit(10)

        with pytest.raises(ValueError):
            editor.add_digit(-1)

    # ---------- Тесты для add_zero() ----------
    def test_add_zero(self):
        editor = ComplexNumberEditor()
        editor.text = "3, -i 1,"
        result = editor.add_zero()
        assert result == "3, -i 10,"

    # ---------- Тесты для backspace() ----------
    def test_backspace_normal(self):
        editor = ComplexNumberEditor()
        editor.text = "12, +i 34,"
        result = editor.backspace()
        assert result == "12, +i 34"

        editor.backspace()
        assert editor.text == "12, +i 3"

    def test_backspace_empty(self):
        editor = ComplexNumberEditor()
        editor._text = ""
        result = editor.backspace()
        assert result == ""

    # ---------- Тесты для clear() ----------
    def test_clear_resets_to_zero(self):
        editor = ComplexNumberEditor()
        editor.text = "999, -i 888,"
        result = editor.clear()
        assert result == "0, +i 0,"
        assert editor.is_zero() is True

    # ---------- Тесты для edit() ----------
    def test_edit_command_1_toggle_sign(self):
        editor = ComplexNumberEditor()
        editor.text = "5, +i 0,"
        editor.edit(1)
        assert editor.text == "-5, +i 0,"

    def test_edit_command_2_add_zero(self):
        editor = ComplexNumberEditor()
        editor.text = "1, +i 2,"
        editor.edit(2)
        assert editor.text == "1, +i 20,"

    def test_edit_command_3_backspace(self):
        editor = ComplexNumberEditor()
        editor.text = "10, +i 0,"
        editor.edit(3)
        assert editor.text == "10, +i 0"

    def test_edit_command_4_clear(self):
        editor = ComplexNumberEditor()
        editor.text = "123, -i 456,"
        editor.edit(4)
        assert editor.text == "0, +i 0,"

    @pytest.mark.parametrize("cmd", [0, 5, 9, 10, 17])
    def test_edit_add_digit_variants(self, cmd):
        editor = ComplexNumberEditor()
        editor.text = "0, +i 0,"
        editor.edit(cmd)
        expected_digit = str(cmd % 10)
        assert editor.text == f"0, +i 0{expected_digit},"

    def test_edit_unknown_command(self):
        editor = ComplexNumberEditor()
        editor.text = "1, +i 1,"
        result = editor.edit(999)
        assert result == "1, +i 1,"

    # ---------- Тесты для _parse_parts() ----------
    def test_parse_parts_valid(self):
        editor = ComplexNumberEditor()
        editor.text = "-12.3, -i 45.6,"
        parts = editor._parse_parts()
        assert parts == ("-12.3", "-", "45.6")

    def test_parse_parts_invalid(self):
        editor = ComplexNumberEditor()
        editor._text = "неправильно"
        assert editor._parse_parts() is None
