

class Heap:
    def __init__(self):
        self.array = []
        self.size = 0


    def _peek(self):
        if self.size == 0:
            return IndexError('Array is empty. Insert value')
        return self.array[0]

    def hasLeftChild(self, index) -> bool:
        return self._getLeftChildIndex(index) < self.size

    def hasRightChild(self, index) -> bool:
        return self._getRightChildIndex(index) < self.size

    def hasParent(self, index) -> bool:
        return self._getParentIndex(index) >= 0

    def _getParentIndex(self, childIndex: int):
        return (childIndex - 1) / 2

    def _getLeftChildIndex(self, parentIndex: int):
        return (2 * parentIndex + 1) / 2
         
    def _getRightChildIndex(self, parentIndex: int):
        return (2 * parentIndex + 2) / 2

    def leftChildNode(self, index):
        return self.array[self._getLeftChildIndex(index)]

    def rightChildNode(self, index):
        return self.array[self._getRightChildIndex(index)]

    def parentNode(self, index):
        return self.array[self._getParentIndex(index)]

    def Swap(self, indexOne: int, indexTwo: int) -> None:
        temp = self.array[indexOne]
        self.array[indexOne] = self.array[indexTwo]
        self.array[indexTwo] = temp

    def Poll(self):
        if self.size == 0:
            raise IndexError('Array is Empty')
        minItem = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return minItem

    def Add(self, item: int):
        self.array[self.size] = item
        self.size += 1
        self.heapifyUp()


    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            minChildIndex = self._getLeftChildIndex()
            if self.hasRightChild(index) and self.rightChildNode(index) < self.leftChildNode(index):
                minChildIndex = self._getRightChildIndex(index)
            if self.array[index] < self.array[minChildIndex]:
                break
            else:
                self.Swap(minChildIndex, index)
            index = minChildIndex
                

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parentNode(index) > self.array[index]:
            self.Swap(self._getParentIndex(index), index)
            index = self._getParentIndex(index)





    
    



