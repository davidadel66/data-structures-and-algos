from core import Array
from typing import Union

class SortedArray: 
    def __init__(self, max_size: int, typecode: str = "l"):
        if max_size <= 0:
            raise ValueError(f"Size needs to be positive: {max_size}")
        self._size = 0
        self._max_size = max_size
        self._array = Array(self._max_size)
        
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            return f"Index is out of range: {index}"
        return self._array[index]
    
    def __repr__(self):
        return f'SortedArray{repr(self._array._array[:self._size])}'
    
    def __iter__(self):
        for i in self._array[:self._size]:
            yield i 
    
    def max_size(self):
        return self._max_size
    
    def insert(self, val: Union[float, int]):
        if self._size >= self._max_size:
            raise ValueError(f'Array is full')
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= val:
                self._array[i] = val
                self._size += 1
                return
            else:
                self._array[i] = self._array[i-1]
        self._array[0] = val
        self._size += 1

    def linear_search(self, target: Union[int, float]) -> Union[int, None]: # O(n)
        for i in self._array[:self._size]:
            if i == target:
                return i
            elif i > target: # If i is bigger than target and array is sorted then there isnt a match. 
                return None
        return None

    def binary_search(self, target: Union[int, float]) -> Union[int, None]:
        left = 0
        right = self._size - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return None
    
    def delete(self, target: Union[int, float]) -> None:
        index = self.binary_search(target)
        if index is None:
            raise ValueError(f'Unable to delete element {target}: the entry is not in the array')
        for i in range(index, self._size, 1):
            self._array[i] = self._array[i+1]
        self._size -= 1

    def find(self, target: Union[int, float]):
        for idx in range(self._size):
            if self._array[idx] == target:
                return idx
        return None


