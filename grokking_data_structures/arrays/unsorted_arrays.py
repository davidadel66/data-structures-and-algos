from core import Array
from typing import Union


class UnsortedArray:
    def __init__(self, max_size: int, typecode: str = 'l'):
        if max_size <= 0:
            raise ValueError(f"Size needs to be positive: {self._size}")
        self._size = 0
        self._max_size = max_size
        self._array = Array(max_size, typecode)

    def __len__(self):
        return self._size

    def __getitem__(self, index: int):
        if index < 0 or index >= self.max_size:
            raise IndexError(f'Index is out of range: {index}')
        return self._array[index]

    def __repr__(self):
        return f'UnsortedArray({repr(self._array._array[:self._size])})'

    def max_size(self):
        return self._max_size

    def insert(self, index: int, val: int) -> None:
        if self._size >= len(self._array):
            raise ValueError('The array is already full')
        self._array[index] = val
        self._size += 1

    def delete(self, index: int):
        if index < 0 or index >= self.max_size:
            raise IndexError(f'Index is out of range: {index}')
        self._array[index] = self._array[self._size - 1]
        self._size -= 1

    def traverse(self, callback: callable):
        for i in range(self._size):
            callback(self._array[i])

    def find(self, target: Union[int, float]) -> int:
        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        return None 
