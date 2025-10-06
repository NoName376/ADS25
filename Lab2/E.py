n = int(input())
names = []
for _ in range(n):
    name = input().strip()
    if names and name == names[-1]:
        continue
    names.append(name)

print(f"All in all: {len(names)}")
print("Students:")
for student in reversed(names):
    print(student)