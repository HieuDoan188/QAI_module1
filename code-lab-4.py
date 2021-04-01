#46
def sum_of_list(lst):
    S = 0
    for i in lst:
        S += i
    return S

lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
print(sum_of_list(lst))


#47
def max3(a, b, c):
    if a>b and a>c:
        return a
    elif b > c:
        return b
    return c

a = int(input())
b = int(input())
c = int(input())
print(max3(a, b, c))

#48
def show(s):
    print("Given string: " + s)
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper +=1
        elif i.islower():
            lower +=1
    print("Number of uppercase letters: " + str(upper))
    print("Number of lowercase letters: " + str(lower))

s = str(input())
show(s)

#49
def get_unique_values(lst):
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(get_unique_values(lst))

#50
def is_prime(n):
    count = 0
    if n < 2:
        return False
    else:
        for i in range(1, n+1):
            if n%i == 0:
                count+=1
        if count == 2:
            return True
        return False

n = int(input())
print(is_prime(n))