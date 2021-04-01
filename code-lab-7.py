# 37
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(min(lst))

# 38
n = int(input())
lst = []
S = 0
for i in range(n):
    lst.append(int(input()))
for i in lst:
    S = S + i
print(S)

# 39
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort()
print(lst)

# 40
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

for i in lst:
    if i%2 == 0:
        lst.remove(i)

print(lst)

# 41
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst1 = []
for i in lst:
    if i%2 != 0:
        lst1.append(i)

print(lst1)

# 41
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst1 = []
for i in lst:
    if i % 5 == 0:
        lst1.append(i)
if len(lst1) == 0:
    lst1.append(0)
print(lst1)