from vector import Vector
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, value):
        n1 = Node(value)
        if self.head is None:
            self.head = n1
            self.tail = n1
        else:
            self.tail.next = n1
            self.tail = n1
    def remove(self, pos):
        n1 = self.head
        if pos == 0:
            self.head = n1.next
        for i in range(pos-1):
            n1 = n1.next
        if n1.next is self.tail:
            self.tail = n1
            n1.next = None
        else:
            n1.next = n1.next.next
    def getValue(self, pos):
        n1 = self.head
        for i in range(pos):
            n1 = n1.next
        return n1.data
    def setValue(self, pos, value):
        n1 = self.head
        for i in range(pos):
            n1 = n1.next
        n1.data = value
    def reverse(self, pos1, pos2):
        p1 = self.head
        p2 = self.head
        for i in range(pos1):
            p1 = p1.next
        for i in range(pos2):
            p2 = p2.next
        if p2 != self.tail:
            n4 = self.head
            for i in range (pos2 + 1):
                n4 = n4.next
        n1 = p1
        n2 = n1.next
        n3 = n2.next
        while n3 is not p2:
            n2.next = n1
            n1 = n2
            n2 = n3
            n3 = n2.next
        n2.next = n1
        n3.next = n2
        if (p2 == self.tail) and (p1 == self.head):
            self.tail = p1
            p1.next = None
            self.head = p2
        elif (p2 == self.tail) and (p1 != self.head):
            n1 = self.head
            for i in range(pos1 - 1):
                n1 = n1.next
            n1.next = n3
            self.tail = p1
            p1.next = None
        elif (p2 != self.tail) and (p1 == self.head):
            p1.next = n4
            self.head = p2
        elif (p2 != self.tail) and (p1 != self.head):
            n1 = self.head
            for i in range(pos1 - 1):
                n1 = n1.next
            n1.next = p2
            p1.next = n4
    def printList(self):
        n1 = self.head
        v = Vector()
        while n1 is not None:
            v.add(n1.data)
            n1 = n1.next
        print(v.getArray())
if __name__ == "__main__":
    l = LinkedList()
    for i in range(1, 11):
        l.add(i)
    l.printList()
    print(l.getValue(5))
    l.setValue(5, 100)
    print(l.getValue(5))
    
    l.remove(9)
    l.printList()

    l.reverse(0,8)
    l.printList()
    l.reverse(0,8)
    l.printList()
    print("")

    l.reverse(4,8)
    l.printList()
    l.reverse(4,8)
    l.printList()
    print("")

    l.reverse(0,4)
    l.printList()
    l.reverse(0,4)
    l.printList()
    print("")

    l.reverse(2,6)
    l.printList()
    l.reverse(1,7)
    l.printList()
    print("")