import pytest

from TMember import TMember

class TestTMember:

    @pytest.mark.parametrize("value1, value2", [(6, 3), (3, 0)])
    def test_init(self, coeff, degree):
        monomial = TMember(coeff, degree)
        
        assert monomial.coeff == coeff
        if coeff == 0:
            assert monomial.degree == 0
        else:
            assert monomial.degree == degree


if __name__ == "__main__":
    pytest.main([__file__, "-v"])