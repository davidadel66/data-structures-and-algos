from core import Node



class Queue:
    def __init__(self, head: Node):
        """
        Follows the idea of FIFO, First-In-First-Out. 

        Enqueue: insert method. Adds another node to the back of the linked list
        Deque: delete method. pops the head of the linked list
        """
        self.head = head
        self.tail = None
        self.length = 0

    def Enqueue(self, value):
        self.length += 1
        newTail = Node(value)
        if not self.tail:
            self.tail = self.head = newTail
            return
        
        self.tail.next = newTail
        self.tail = newTail

    def Deque(self):
        if not self.head:
            return None

        self.length -= 1
        tempHead = self.head
        self.head = self.head.next
        
        return tempHead.val

    def Peek(self):
        if self.head:
            peekHead = self.head
            return peekHead.val

    def __repr__(self):
        viewList = []
        curr = self.head
        while curr:
            viewList.append(curr.val)
            curr = curr.next
        return str(viewList)
            


if __name__ == "__main__":
    head = Node(0)
    queue = Queue(head)

    for i in range(10):
        newNode = Node(i)
        queue.Enqueue(newNode)


    print(queue)

    queue.Deque()

    print(queue)
        

