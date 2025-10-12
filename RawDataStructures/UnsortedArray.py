from core import Array
from typing import Callable


class UnsortedArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._size = 0
        self._array = Array(capacity)

    def __len__(self):
        return self._size

    def find_index(self, index):
        if index < 0 or index > self._size:
            print('Invalid index')
        return self._array[index]

    def find_value(self, value):
        if self._size == 0:
            print('Array size is 0')
            return 

        for i in range(self._size):
            if self._array[i] == value:
                print(i, value)
                return i
        return None

    def insert(self, value):
        self._array[self._size] = value
        self._size += 1

    def delete_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError('Index is out of range')

        self._array[index] = self._array[self._size - 1]
        self._array[self._size - 1] = 0
        self._size -= 1

    def traverse(self, callback: Callable):
        for i in range(self._size):
            callback(self._array[i])


    def delete_value(self, value): 
        index = self.find_value(value)
        if index == self._size - 1:
            self._array[index] = 0
            self._size -= 1
        else:
            self.delete_index(index)

    def __getitem__(self, index: int):
        if index < 0 or index > self._size:
            raise IndexError('Index is out of range')
        return self._array[index] 

    def __setitem__(self, index, val):
        if index < 0 or index > self._size:
            print(index, self._size)
            raise IndexError('Index is out of range')
        self._array[index] = val

    def __repr__(self):
        return repr(self._array._array)


