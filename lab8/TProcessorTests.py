import pytest

from TProcessor import TProcessor, Operations, Functions


class TestTProc:
    
    def test_init_without_args(self):
        proc = TProcessor()
        assert proc.lop == 0
        assert proc.rop == 0
        assert proc.operation == Operations.NONE
    
    @pytest.mark.parametrize("value1, value2", [(5, 9)])
    def test_init_with_args(self, value1, value2):
        proc = TProcessor(value1, value2)
        assert proc.lop == value1
        assert proc.rop == value2
        assert proc.operation == Operations.NONE

    @pytest.mark.parametrize("value1, value2", [(5, 9)])
    def test_reset_processor(self, value1, value2):
        proc = TProcessor(value1, value2)
        proc.reset_processor()
        assert proc.lop == 0
        assert proc.rop == 0
        assert proc.operation == Operations.NONE

    @pytest.mark.parametrize("value1, value2", [(5, 9)])
    def test_reset_operation(self, value1, value2):
        proc = TProcessor(value1, value2)
        proc.operation = Operations.ADD
        proc.reset_operation()
        assert proc.operation == Operations.NONE

    @pytest.mark.parametrize("value1, value2", [(5, 9)])
    def test_execute_operation_add(self, value1, value2):
        proc = TProcessor(value1, value2)
        proc.operation = Operations.ADD
        proc.execute_operation()

        assert proc.lop == value1 + value2

    @pytest.mark.parametrize("value1, value2", [(5, 9)])
    def test_execute_operation_sub(self, value1, value2):
        proc = TProcessor(value1, value2)
        proc.operation = Operations.SUB
        proc.execute_operation()

        assert proc.lop == value1 - value2

    @pytest.mark.parametrize("value1, value2", [(5, 9)])
    def test_execute_operation_mul(self, value1, value2):
        proc = TProcessor(value1, value2)
        proc.operation = Operations.MUL
        proc.execute_operation()

        assert proc.lop == value1 * value2

    @pytest.mark.parametrize("value1, value2", [(5, 9)])
    def test_execute_operation_mul(self, value1, value2):
        proc = TProcessor(value1, value2)
        proc.operation = Operations.DIV
        proc.execute_operation()

        assert proc.lop == value1 / value2

    @pytest.mark.parametrize("value", [25])
    def test_execute_func_reverse(self, value):
        proc = TProcessor()
        proc.rop = value
        proc.execute_function(Functions.REVERSE)

        assert proc.rop == int(str(value)[::-1])

    @pytest.mark.parametrize("value", [25])
    def test_execute_func_reverse(self, value):
        proc = TProcessor()
        proc.rop = value
        proc.execute_function(Functions.SQUARE)

        assert proc.rop == value ** 2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
