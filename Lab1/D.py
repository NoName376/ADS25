s = input().strip()

if not s:
    print("NO")
else:
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    print("YES" if not stack else "NO")