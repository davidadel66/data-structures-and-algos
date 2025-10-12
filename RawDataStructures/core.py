import array
from typing import Union


class Array:
    def __init__(self, size: int, typecode: str = 'd'):
        if size <= 0:
            raise ValueError('Value needs to be higher than 0')
        self._size = size
        self._array = array.array(typecode, size * [0])

    def __len__(self):
        return self._size

    def __getitem__(self, index: int):
        if index < 0 or index > self._size:
            raise IndexError('Index is out of range')
        return self._array[index] 

    def __setitem__(self, index: int, value: Union[int, float]) -> None:
        if index < 0 or index > self._size:
            raise IndexError('Index is out of range')
        self._array[index] = value

    def __repr__(self):
        return repr(self._array)



