import sys, os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TMember import TMember
from TPoly import TPoly

def test_member_constructor_zero():
    m = TMember(0, 5)
    assert m.read_coeff() == 0
    assert m.read_degree() == 0


def test_member_constructor_nonzero():
    m = TMember(6, 3)
    assert m.read_coeff() == 6
    assert m.read_degree() == 3


def test_member_write_and_read():
    m = TMember()
    m.write_coeff(7)
    m.write_degree(4)
    assert m.read_coeff() == 7
    assert m.read_degree() == 4


def test_member_is_equal():
    a = TMember(2, 2)
    b = TMember(2, 2)
    c = TMember(3, 2)
    assert a.is_equal(b)
    assert not a.is_equal(c)


def test_member_differentiate_basic():
    a = TMember(3, 3)
    d = a.differentiate()
    assert isinstance(d, TMember)
    assert d.read_coeff() == 9
    assert d.read_degree() == 2


def test_member_compute_and_str():
    # compute: 2 * (2**3) = 16
    a = TMember(2, 3)
    assert pytest.approx(a.compute(2.0)) == 16.0

    # string representations
    cases = [
        (TMember(3, 0), "3"),
        (TMember(1, 1), "x"),
        (TMember(-1, 1), "-x"),
        (TMember(2, 1), "2x"),
        (TMember(1, 2), "x^2"),
        (TMember(-1, 3), "-x^3"),
    ]
    for member, expected in cases:
        assert str(member) == expected


# -----------------
# TPoly tests
# -----------------

def test_poly_constructor_zero():
    p = TPoly()
    assert hasattr(p, "polynom")
    assert len(p.polynom) == 0
    assert p.max_degree() == 0


def test_poly_constructor_single_monom():
    p = TPoly(5, 2)  # 5x^2
    assert p.max_degree() == 2
    assert p.coeff(2) == 5


def test_poly_clear():
    p = TPoly(1, 1)
    p.clear()
    assert len(p.polynom) == 0
    assert p.max_degree() == 0


def test_poly_elem_and_getitem():
    # build polynomial 3x^3 + 2x + 1 using public constructor and addition
    p = TPoly(3, 3) + TPoly(2, 1) + TPoly(1, 0)
    top = p.elem(0)
    assert isinstance(top, TMember)
    assert top.read_coeff() == 3
    assert top.read_degree() == 3
    # __getitem__ delegates to elem
    assert p[1].read_degree() == 1


def test_poly_coeff_method():
    p = TPoly(4, 2)
    assert p.coeff(2) == 4
    assert p.coeff(3) == 0


def test_poly_add_sub_mul_minus():
    p1 = TPoly(3, 2) + TPoly(1, 0)  # 3x^2 + 1
    p2 = TPoly(2, 1) + TPoly(1, 0)  # 2x + 1

    s = p1 + p2  # expected 3x^2 + 2x + 2
    assert s.coeff(2) == 3
    assert s.coeff(1) == 2
    assert s.coeff(0) == 2

    r = p1 - p2  # expected 3x^2 - 2x
    assert r.coeff(2) == 3
    assert r.coeff(1) == -2
    assert r.coeff(0) == 0 or 0 not in r.polynom

    m = p1 * p2  # (3x^2+1)*(2x+1) = 6x^3 + 3x^2 + 2x + 1
    assert m.coeff(3) == 6
    assert m.coeff(2) == 3
    assert m.coeff(1) == 2
    assert m.coeff(0) == 1

    neg = p2.minus()  # -2x -1
    assert neg.coeff(1) == -2
    assert neg.coeff(0) == -1


def test_poly_differentiate_and_compute_and_repr():
    p = TPoly(1, 3) + TPoly(7, 1) + TPoly(5, 0)  # x^3 + 7x + 5
    d = p.differentiate()  # expected 3x^2 + 7
    assert d.coeff(2) == 3
    assert d.coeff(0) == 7

    # compute (x^2 + 3x) at x=2 equals 10
    p2 = TPoly(1, 2) + TPoly(3, 1)
    assert pytest.approx(p2.compute(2.0)) == 10.0

    # __repr__ should produce a readable string
    r = repr(p2)
    assert isinstance(r, str)
