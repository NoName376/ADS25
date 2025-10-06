class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
        self.size += 1

    def to_list(self):
        result_list = []
        current = self.head
        while current:
            result_list.append(current.data)
            current = current.next
        return result_list

def find_modes(llist):
    elements = llist.to_list()
    if not elements:
        return []

    counts = {}
    for element in elements:
        counts[element] = counts.get(element, 0) + 1

    max_count = 0
    for count in counts.values():
        if count > max_count:
            max_count = count

    modes = []
    for element, count in counts.items():
        if count == max_count:
            modes.append(element)
    
    modes.sort(reverse=True)
    return modes

def solve():
    n = int(input())
    if n == 0:
        return

    numbers = list(map(int, input().split()))

    llist = LinkedList()
    for number in numbers:
        llist.append(number)
    
    modes = find_modes(llist)
    print(*modes)

if __name__ == "__main__":
    solve()