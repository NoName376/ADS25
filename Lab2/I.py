class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        print("ok")

    def add_back(self, val):
        node = Node(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        print("ok")

    def erase_front(self):
        if not self.head:
            print("error")
            return
        print(self.head.val)
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def erase_back(self):
        if not self.tail:
            print("error")
            return
        print(self.tail.val)
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def front(self):
        if self.head:
            print(self.head.val)
        else:
            print("error")

    def back(self):
        if self.tail:
            print(self.tail.val)
        else:
            print("error")

    def clear(self):
        self.head = self.tail = None
        print("ok")

dll = DoublyLinkedList()

while True:
    parts = input().split()
    cmd = parts[0]
    if cmd == "exit":
        print("goodbye")
        break
    if cmd == "add_front":
        dll.add_front(parts[1])
    elif cmd == "add_back":
        dll.add_back(parts[1])
    elif cmd == "erase_front":
        dll.erase_front()
    elif cmd == "erase_back":
        dll.erase_back()
    elif cmd == "front":
        dll.front()
    elif cmd == "back":
        dll.back()
    elif cmd == "clear":
        dll.clear()