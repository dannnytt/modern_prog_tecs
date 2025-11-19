import pytest

from TSet import TSet


class TestTSet:

    def test_method_init(self):
        my_set: TSet[int] = TSet[int]()
        assert isinstance(my_set, TSet)
        assert len(my_set) == 0 

    def test_method_clear(self):
        my_set: TSet[int] = TSet[int]()
        my_set.insert(1)
        my_set.clear()
        assert len(my_set) == 0

    def test_method_insert(self):
        my_set: TSet[int] = TSet[int]()
        my_set.insert(1)
        assert len(my_set) == 1
        
        added_elem: int = my_set.element(0)
        assert added_elem == 1

    def test_method_remove(self):
        my_set: TSet[int] = TSet[int]()
        my_set.insert(5)
        assert len(my_set) == 1

        my_set.remove(5)
        assert len(my_set) == 0

    def test_when_is_empty(self):
        my_set: TSet[int] = TSet[int]()
        assert my_set.is_empty()

    def test_when_is__not_empty(self):
        my_set: TSet[int] = TSet[int]()
        my_set.insert(5)
        assert not my_set.is_empty()

    def test_when_contains(self):
        my_set: TSet[int] = TSet[int]()
        my_set.insert(5)
        assert my_set.contains(5)

    def test_when_not_contains(self):
        my_set: TSet[int] = TSet[int]()
        assert not my_set.contains(5)

    def test_method_add(self):
        set1: TSet[int] = TSet[int]()
        set1.insert(1)
        set1.insert(2)

        set2: TSet[int] = TSet[int]()
        set2.insert(2)
        set2.insert(3)

        result: TSet[int] = set1.add(set2)

        assert len(result) == 3
        assert result.contains(1)
        assert result.contains(2)
        assert result.contains(3)
        assert not result.contains(4)

    def test_method_subtract(self):
        set1: TSet[int] = TSet[int]()
        set1.insert(1)
        set1.insert(2)
        set1.insert(3)

        set2: TSet[int] = TSet[int]()
        set2.insert(2)
        set2.insert(4)

        result: TSet[int] = set1.subtract(set2)

        assert len(result) == 2
        assert result.contains(1)
        assert result.contains(3)
        assert not result.contains(2)
        assert not result.contains(4)

    def test_method_multiply(self):
        set1: TSet[int] = TSet[int]()
        set1.insert(1)
        set1.insert(2)
        set1.insert(3)

        set2: TSet[int] = TSet[int]()
        set2.insert(2)
        set2.insert(3)
        set2.insert(4)

        result = set1.multiply(set2)

        assert len(result) == 2
        assert result.contains(2)
        assert result.contains(3)
        assert not result.contains(1)
        assert not result.contains(4)

    def test_method_count(self):
        my_set: TSet[int] = TSet[int]()
        my_set.insert(3)
        my_set.insert(2)
        my_set.insert(1)

        assert len(my_set) == my_set.count()

    def test_method_element(self):
        my_set: TSet[int] = TSet[int]()
        my_set.insert(3)
        my_set.insert(2)
        my_set.insert(1)

        elements = {my_set.element(i) for i in range(len(my_set))}
        assert elements == {1, 2, 3}

    

if __name__ == "__main__":
    pytest.main([__file__, "-v"])