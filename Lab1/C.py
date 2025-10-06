data = input().split()
s = data[0]
t = data[1] if len(data) > 1 else ''

def process(string):
    res = []
    for ch in string:
        if ch == '#':
            if res:
                res.pop()
        else:
            res.append(ch)
    return ''.join(res)

print("Yes" if process(s) == process(t) else "No")