class Node:
    def __init__(self, data, next_node = None, prev_node = None):
        self._data = data
        self._next = next_node
        self._prev = prev_node

    def data(self):
        return self._data

    def has_next(self):
        return self._next is not None

    def has_prev(self):
        return self._prev is not None

    def prev(self):
        return self._prev
    
    def next(self):
        return self._next

    def append(self, next_node):
        self._next = next_node


class SinglyLinkedList:
    def __init__(self): 
        self._head = None

    def insert_to_back(self, data):
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))

    def insert_to_front(self, data: Node):
        if self._head is None:
            self._head = Node(data)
        else:
            old_head = self._head
            self._head = Node(data, old_head)
            
    def _search(self, target):
        current = self._head
        previous = None
        while current and current.data() != target:
            previous = current
            current = current.next()
        return current, previous
        
    def _delete(self, target):
        node_to_delete, previous = self._search(target)
        if node_to_delete == self._head:
            new_head = node_to_delete.next()
            self._head = new_head
        elif node_to_delete.next() is None:
            previous._next = None
        else:
            replacement_node = node_to_delete.next()
            previous._next = replacement_node

    def print_list(self):
        nodes = []
        current = self._head
        while current:
            nodes.append(str(current.data()))
            current = current.next()
        print(" <-> ".join(nodes))

class DoublyLinkedList():
    def __init__(self):
        self._head = None

    def insert_to_front(self, data):
        if self._head is None:
            self._head = Node(data)
        else:
            old_head = self._head
            new_head = Node(data, old_head)
            old_head.prev = new_head
            self._head = new_head

    def insert_to_back(self, data):
        if self._head is None:
            self._head = Node(data)
            return

        current = self._head
        while current.next():
            current = current.next()
        current.append(Node(data))
        prev = current
        current = current.next()
        current.prev = prev

    def _search(self, target):
        current = self._head
        while current and current.data() != target:
            current = current.next()
        return current

    def _delete(self, target):
        node_to_delete = self._search(target)

        if node_to_delete is None:
            return 

        prev_node = node_to_delete.prev()
        next_node = node_to_delete.next()

        if prev_node is None:
            self._head = next_node
        else:
            prev_node._next = next_node

        if next_node is not None:
            next_node._prev = prev_node

    def print_list(self):
        nodes = []
        current = self._head
        while current:
            nodes.append(str(current.data()))
            current = current.next()
        print(" <-> ".join(nodes))
