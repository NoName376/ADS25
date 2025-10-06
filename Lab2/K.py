class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMaxSum(n: int, head: ListNode) -> int:
    if not head:
        return 0
    
    max_so_far = head.val
    current_max = head.val
    
    current_node = head.next
    while current_node:
        current_max = max(current_node.val, current_max + current_node.val)
        max_so_far = max(max_so_far, current_max)
        current_node = current_node.next
        
    return max_so_far

def solve():
    n_str = input()
    if not n_str:
        return
    n = int(n_str)
    
    a = list(map(int, input().split()))
    
    head = None
    if n > 0:
        head = ListNode(a[0])
        tail = head
        for i in range(1, n):
            tmp = ListNode(a[i])
            tail.next = tmp
            tail = tmp

    print(findMaxSum(n, head))

if __name__ == "__main__":
    solve()