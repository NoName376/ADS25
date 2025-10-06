class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_second_elements(self):
        if not self.head or not self.head.next:
            return

        prev = self.head
        current = self.head.next
        
        while current:
            prev.next = current.next
            prev = prev.next
            if prev:
                current = prev.next
            else:
                current = None

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(' '.join(elements))

def solve():
    n_str = input()
    if not n_str:
        return
    n = int(n_str)
    
    if n <= 0:
        return

    elements_str = input()
    if not elements_str:
        return
    elements = list(map(int, elements_str.split()))

    llist = LinkedList()
    for element in elements:
        llist.append(element)

    llist.delete_second_elements()
    llist.print_list()

if __name__ == "__main__":
    solve()