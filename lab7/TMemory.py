from enum import Enum

class MemoryState(Enum):
    OFF = 'Off'
    ON = 'On'

class TMemory:
    
    def __init__(self, number=None):
        self._number = number if number is not None else 0
        self._state = MemoryState.OFF
    
    def store(self, value):
        self._number = value
        self._state = MemoryState.ON

    def get(self):
        self._state = MemoryState.ON 
        return self._number
    
    def add(self, value):
        self._number += value
        self._state = MemoryState.ON 

    def clear(self):
        self._number = 0
        self._state = MemoryState.OFF

    @property
    def state(self):
        return self._state
    
    @property
    def number(self):
        return self._number