import array
from typing import Union

class Array:
    def __init__(self, size: int, typecode: str = 'l'):
        if size <= 0:
            raise ValueError(f'Invalid array size (must be positive): {size}')
        self._size = size
        self._array = array.array(typecode, [0] * size)

    def __len__(self):
        return self._size
    
    def __getitem__(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError('array index out of range')
        return self._array[index]
    
    def __setitem__(self, index: int, val: Union[int, float]) -> None:
        if index < 0 or index >= self._size:
            raise IndexError('array assignment index out of range')
        self._array[index] = val

    def __repr__(self):
        return repr(self._array)
