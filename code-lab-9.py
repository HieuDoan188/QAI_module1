# 51
#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)


def evenNum(res):
    return list(filter(lambda x: x%2==0,res))

print(evenNum(res))


# 52
a = int(input())
b = int(input())

def power(a, b):
    return a**b

print(power(a,b))

#53
a = int(input())
b = int(input())

def gcd(a,b):
    count = 1
    result = 1
    while count<= min(a,b):
        if a%count==0 and b%count==0:
            if result <= count:
                result = count
                count+=1
        else:
            count+=1
    return result
print(gcd(a,b))

#54
a = int(input())
b = int(input())
c = int(input())

if a == b and a==c and b==c:
    print("Equilateral triangle")
elif a == b or a==c or b==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")