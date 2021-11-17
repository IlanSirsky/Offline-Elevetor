class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head:Node = None
        self.tail:Node = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            temp = Node(val)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def addlast(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            temp = Node(val)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp

    def getFirst(self):
        return self.head.val

    def getLast(self):
        return self.tail.val

    def delete(self):
        self.head = self.head.next

    def __repr__(self):
        return f"Head: {self.head}, Tail: {self.tail}"
