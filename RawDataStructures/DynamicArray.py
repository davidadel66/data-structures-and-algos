from arrays.core import Array
from typing import Union


class DynamicSortedArray:
    def __init__(self, capacity: int = 1, typecode: str = 'l'):
        self.capacity = capacity
        self.typecode = typecode
        self._array = Array(size=self.capacity, typecode=self.typecode)
        self._size = 0

    def insert(self, value):
        if self._size >= self.capacity:
            self._double_array_size()
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self.array[i-1]
        self._array[0] = value
        self._size += 1

    def _double_array_size(self):
        old_array = self._array
        self._array = Array(size=self.capacity*2, typecode=self.typecode)
        self.capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i]

    def _shrink_array_size(self):
        old_array = self._array
        self._array = Array(size=self.capacity/2, typecode=self.typecode)
        self.capacity /= 2
        for i in range(self._size):
            self._array[i] = old_array[i]

    def delete_by_index(self, index: int):
        if index < 0 or index >= self._size:
            raise ValueError('Index is out of range')
        for i in range(index, self._size - 1, 1):
            self._array[i] = self._array[i+1]
        self._size -= 1

        if self._size > 0 and self._size <= self.capacity//4:
            self._shrink_array_size()

    def delete_by_value(self, value: Union[int, float]):
        index = self.find(value)
        if index:
            for i in range(index, self._size - 1, 1):
                self._array[i] = self._array[i+1]
            self._size -= 1
        if self._size > 0 and self._size <= self.capacity//4:
            self._shrink_array_size()




    def linear_find(self, value: Union[int, float]):
        for i in range(len(self._array)):
            if self._array[i] == value:
                return i
        return None


    def traverse(self, callback: callable):
        for i in range(self._size):
            callback(self._array[i])




