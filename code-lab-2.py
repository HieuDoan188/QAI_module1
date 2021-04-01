#8
num_integer =  5000
num_float = 1.2345
string_var = "Codelearn.io"
boolean_var = False

print(num_integer)
print(num_float)
print(string_var)
print(boolean_var)

#9
name = "Codelearn"
print("Hello " + name)

#10
name = "Codelearn"
date_of_birth = 2019
print("Name: " + name)
print("Date of birth: " + str(date_of_birth))

#11
a = 438
b = 636

print("a + b = " + str(a+b))
print("a - b = " + str(a-b))
print("a * b = " + str(a*b))
print("a / b = " + str(a/b))

#12
length = 7.8
width = 3.5

print("Area: " + str(length*width))
print("Perimeter: " + str((length+width)*2))

#13
a = input()
print("Hello " + a)

#14
a = input()
b = int(input())
print("In 15 years, age of " + a + " will be " + str(b+15))

#15
a = int(input())
b = int(input())

print("a % b = " + str(a%b))

#16
a = int(input())
b = int(input())

print("a + b = " + str(a+b))
print("a - b = " + str(a-b))
print("a * b = " + str(a*b))
print("a / b = " + str(a/b))
print("a % b = " + str(a%b))

#17
a = int(input())
b = int(input())
c = a
a = b
b = c
print("after swap a = " + str(a) + ", b = " + str(b))

#18
a = float(input())
print("Circumference = " + str(2*3.14*a))

#19
a = int(input())
h = int(input())
area = a*h/2
print("The area of triangle is " + str(area))

#20
a = int(input())
b = int(input())
print(a**b)

#21
x = int(input())
y = int(input())
print("x > y: " + str(x>y))

#22
a = int(input())
Total = int(input())
Total += a # Using += Operator
print("The Value of the Total after using += Operator is:", Total)
Total -= a # Using -= Operator
print("The Value of the Total after using -= Operator is:", Total)
Total *= a # Using *= Operator
print("The Value of the Total after using *= Operator is:", Total)
Total //= a # Using //= Operator
print("The Value of the Total after using //= Operator is:", Total)
Total **= a # Using **= Operator
print("The Value of the Total after using **= Operator is:", Total)
Total /= a # Using /= Operator
print("The Value of the Total after using /= Operator is:", Total)
Total %= a # Using %= Operator
print("The Value of the Total after using %= Operator is:", Total)

#23
x = input()
print('H' in x)

#24
a = int(input())
b = int(input())
print(a == b)

#25
x = int(input())
y = int(input())
z = int(input())
t = int(input())
print("Result evaluation is", (x > y) and (z < t))