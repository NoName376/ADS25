from collections import deque

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        stream = input().split()
        
        freq = [0] * 26
        queue = deque()
        result = []
        
        for char in stream:
            char_index = ord(char) - ord('a')
            
            freq[char_index] += 1
            
            if freq[char_index] == 1:
                queue.append(char)
            
            while queue and freq[ord(queue[0]) - ord('a')] > 1:
                queue.popleft()
            
            if queue:
                result.append(queue[0])
            else:
                result.append('-1')
                
        print(' '.join(result))

if __name__ == "__main__":
    solve()