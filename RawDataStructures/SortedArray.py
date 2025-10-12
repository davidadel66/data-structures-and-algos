from UnsortedArray import UnsortedArray

class SortedArray(UnsortedArray):
    def __init__(self, capacity):
        super().__init__(capacity)

    def insert(self, value):
        i = 0
        while i < self._size and self._array[i] < value:
            i += 1

        for j in range(self._size, i, -1):
            self._array[j] = self._array[j-1]

        self._array[i] = value
        self._size += 1

    def find_value(self, value):
        i = 0
        j = self._size - 1

        while i <= j: 
            mid = (j + i) // 2
            if self._array[mid] == value:
                return mid
            elif self._array[mid] > value:
                j = mid - 1
            else:
                i = mid + 1

    def delete_index(self, index: int):
        if index < 0 or index >= self._size: 
            raise IndexError('Index out of range')

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i+1]

        self._array[self._size - 1] = 0
        self._size -= 0

    def __setitem__(self, index: int, val):
        """Disallow direct setting as it can break the sorted order."""
        raise NotImplementedError(f"Cannot set item directly in a SortedArray. Use insert({val}).")

