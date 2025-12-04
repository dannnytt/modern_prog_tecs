from __future__ import annotations

from typing import TypeVar, Generic

T = TypeVar('T')

class TSet(Generic[T]):
    
    def __init__(self) -> None:
        self.__container: set[T] = set()
    
    def clear(self) -> None:
        self.__container.clear()

    def insert(self, value: T) -> None:
        self.__container.add(value)

    def remove(self, value: T) -> None:
        self.__container.discard(value)

    def is_empty(self) -> bool:
        return len(self.__container) == 0
    
    def contains(self, value: T) -> bool:
        return value in self.__container
    
    def add(self, other_set: TSet[T]) -> TSet[T]:
        result = TSet[T]()
        result.__container = self.__container | other_set.__container
        return result
    
    def subtract(self, other_set: TSet) -> TSet:
        result = TSet[T]()
        result.__container = self.__container - other_set.__container
        return result
    
    def multiply(self, other_set: TSet) -> TSet:
        result = TSet[T]()
        result.__container = self.__container & other_set.__container
        return result
    
    def count(self) -> int:
        return len(self.__container)
    
    def element(self, num: int) -> T:
        if num < 0 or num >= len(self.__container): 
            raise IndexError("incorrect index.")
        return list(self.__container)[num] 
    
    def __len__(self) -> int:
        return len(self.__container)
    
    @property
    def container(self) -> set[T]:
        return self.__container
