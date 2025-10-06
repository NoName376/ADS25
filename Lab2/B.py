class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def solve():
    line1 = input().split()
    n = int(line1[0])
    k = int(line1[1])

    if n == 0:
        return

    words = input().split()

    head = Node(words[0])
    current = head
    for i in range(1, n):
        current.next = Node(words[i])
        current = current.next

    def shift_list(head, n, k):
        if not head or n == 0:
            return None

        k %= n
        if k == 0:
            return head

        current = head
        for _ in range(k - 1):
            current = current.next
        
        new_head = current.next
        current.next = None

        tail = new_head
        while tail.next:
            tail = tail.next
        
        tail.next = head

        return new_head

    new_head = shift_list(head, n, k)

    output = []
    current = new_head
    while current:
        output.append(current.data)
        current = current.next
    
    print(' '.join(output))

if __name__ == "__main__":
    solve()