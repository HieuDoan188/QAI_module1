#31
n = int(input())
S = 0
for i in range(n+1):
    S = S + i
print(S)

#32
a = int(input())
b = int(input())

S = 0
while b>=a:
    if a%2 != 0:
        S = S + a
    a+=1
print(S)

#33
s = input()
for c in s:
    if c != "y":
        print("Current character:", c)

#34
n = int(input())
b = 1

while b <= 5:
    print("%s * %s = %s" %(str(n),str(b),(str(n*b))))
    b+=1

#35
#Input
a = int(input())
b = int(input())
count_odd = 0
count_even = 0

while a<=b:
    if a%2 == 0:
        count_even+=1
    else:
        count_odd+=1
    a+=1

print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)

#36
n = int(input())
S = 0
for i in range(n+1):
    S = S + i/(i+1)

print(round(S,2))