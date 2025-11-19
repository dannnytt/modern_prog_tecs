import pytest
from TPNumber import TPNumber


class TestTPNumber:

    def test_init_base_too_low(self):
        with pytest.raises(ValueError):
            TPNumber(1.0, 1, 0)
    
    def test_init_base_too_high(self):
        with pytest.raises(ValueError):
            TPNumber(1.0, 17, 0)

    def test_init_negative_accuracy(self):
        with pytest.raises(ValueError):
            TPNumber(1.0, 10, -1)

    
    @pytest.mark.parametrize("a1, b1, c1, a2, b2, c2",[
        (1.0, 10, 2, 2.0, 10, 3),
        (5.5, 2, 1, 4.5, 2, 4),
    ])
    def test_add(self, a1, b1, c1, a2, b2, c2):
        n1 = TPNumber(a1, b1, c1)
        n2 = TPNumber(a2, b2, c2)

        result = n1.add(n2)

        assert result.p_num == a1 + a2
        assert result.base_num == b1
        assert result.accuracy_num == max(c1, c2)
    
    
    @pytest.mark.parametrize("a1, b1, c1, a2, b2, c2", [
        (1.0, 10, 2, 2.0, 10, 3),
        (5.5, 2, 1, 4.5, 2, 4),
    ])
    def test_multiply(self, a1, b1, c1, a2, b2, c2):
        n1 = TPNumber(a1, b1, c1)
        n2 = TPNumber(a2, b2, c2)

        result = n1.multiply(n2)
        assert result.p_num == a1 * a2
        assert result.base_num == b1
        assert result.accuracy_num == max(c1, c2)


    @pytest.mark.parametrize("a1, b1, c1, a2, b2, c2", [
        (1.0, 10, 2, 2.0, 10, 3),
        (5.5, 2, 1, 4.5, 2, 4),
    ])
    def test_subtract(self, a1, b1, c1, a2, b2, c2):
        n1 = TPNumber(a1, b1, c1)
        n2 = TPNumber(a2, b2, c2)

        result = n1.subtract(n2)
        assert result.p_num == a1 - a2
        assert result.base_num == b1
        assert result.accuracy_num == max(c1, c2)


    @pytest.mark.parametrize("a1, b1, c1, a2, b2, c2", [
        (1.0, 10, 2, 2.0, 10, 3),
        (5.5, 2, 1, 4.5, 2, 4),
    ])
    def test_divide(self, a1, b1, c1, a2, b2, c2):
        n1 = TPNumber(a1, b1, c1)
        n2 = TPNumber(a2, b2, c2)

        result = n1.divide(n2)
        assert result.p_num == a1 / a2
        assert result.base_num == b1
        assert result.accuracy_num == max(c1, c2)


    @pytest.mark.parametrize("a1, b1, c1, a2, b2, c2", [
        (5.0, 10, 2, 0.0, 10, 2),
        (5.0, 8, 2, 0.0, 8, 2)
    ])
    def test_divide_with_with_zero_num(self, a1, b1, c1, a2, b2, c2):
        with pytest.raises(ValueError):
            n1 = TPNumber(a1, b1, c1)
            n2 = TPNumber(a2, b2, c2)
            
            resn = n1.divide(n2)

    
    @pytest.mark.parametrize("a, b, c", [
        (1.0, 10, 2),
        (5.5, 2, 1),
    ])
    def test_reverse(self, a, b, c):
        n = TPNumber(a, b, c)

        result = n.reverse()
        assert result.p_num == 1 / a
        assert result.base_num == b
        assert result.accuracy_num == c


    @pytest.mark.parametrize("a, b, c", [
        (0.0, 10, 2),
        (0.0, 8, 3)
    ])
    def test_reverse_with_zero_num(self, a, b, c):
        with pytest.raises(ValueError):
            n = TPNumber(a, b, c)
            res = n.reverse()


if __name__ == "__main__":
    pytest.main([__file__])