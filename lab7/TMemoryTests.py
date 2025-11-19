import pytest

from TMemory import TMemory, MemoryState

class TestTMemory:
    
    def test_init_without_args(self):
        mem = TMemory()
        assert mem.number == 0
        assert mem.state == MemoryState.OFF

    @pytest.mark.parametrize("value", [5, 3.14])
    def test_init_with_arg(self, value):
        mem = TMemory(value)
        assert mem.number == value
        assert mem.state == MemoryState.OFF
    
    @pytest.mark.parametrize("value", [5, 3.14])
    def test_store(self, value):
        mem = TMemory()
        mem.store(value)
        assert mem.number == value
        assert mem.state == MemoryState.ON

    @pytest.mark.parametrize("value", [5, 3.14])
    def test_get(self, value):
        mem = TMemory()
        mem.store(value)
        stored =  mem.get()
        assert stored == value
        assert mem.state == MemoryState.ON

    @pytest.mark.parametrize("value1, value2", [(5, 3.14)])
    def test_add(self, value1, value2):
        mem = TMemory()
        mem.store(value1)
        mem.add(value2)
        assert mem.number == value1 + value2
        assert mem.state == MemoryState.ON
    
    @pytest.mark.parametrize("value", [5, 3.14])
    def test_clear(self, value):
        mem = TMemory()
        mem.store(value)
        mem.clear()
        assert mem.number == 0
        assert mem.state == MemoryState.OFF

    @pytest.mark.parametrize("value", [5, 3.14])
    def test_read_state1(self, value):
        mem = TMemory(value)
        assert mem.state == MemoryState.OFF

    @pytest.mark.parametrize("value", [5, 3.14])
    def test_read_state2(self, value):
        mem = TMemory()
        mem.store(value)
        assert mem.state == MemoryState.ON

    @pytest.mark.parametrize("value", [5, 3.14])
    def test_read_number(self, value):
        mem = TMemory(value)
        assert mem.number == value
        assert mem.state == MemoryState.OFF

if __name__ == "__main__":
    pytest.main([__file__, "-v"])