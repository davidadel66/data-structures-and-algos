from core import Node


class Stack: # Last-In-First-Out
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        self.length += 1
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
    
    def pop(self):
        if self.length == 0:
            return IndexError('Stack has no nodes left')
        self.length -= 1
        tempHead = self.head
        self.head = self.head.next

        return tempHead.val

    def peek(self):
        if self.head:
            return self.head.val
    

    def __repr__(self):
        curr = self.head
        printList = []
        while curr:
            printList.append(curr.val)
            curr = curr.next

        return str(printList)



if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.pop()
    stack.push(0)

    


    print(stack)


