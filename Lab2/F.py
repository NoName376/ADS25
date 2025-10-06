class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insertNodeAtPosition(head, data, position):
    new_node = Node(data)
    
    if position == 0:
        new_node.next = head
        return new_node
    
    current = head
    for _ in range(position - 1):
        current = current.next
        
    new_node.next = current.next
    current.next = new_node
    
    return head

def solve():
    n_str = input()
    if not n_str:
        return
    n = int(n_str)
    
    head = None
    if n > 0:
        head = Node(int(input()))
        current = head
        for _ in range(n - 1):
            current.next = Node(int(input()))
            current = current.next
    
    data_to_insert = int(input())
    position = int(input())
    
    new_head = insertNodeAtPosition(head, data_to_insert, position)
    
    output = []
    current = new_head
    while current:
        output.append(str(current.data))
        current = current.next
    
    print(' '.join(output))

if __name__ == "__main__":
    solve()