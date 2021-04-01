# 42
s = input()
print(s.upper())

# 43
s = input()
l = len(s)
if s != "a":
    print(s[0:2]+s[l-2:l])
else:
    print("")

# 44
s1 = input()
s2 = input()

s3 = s1[0:2] + s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = s3
print(s1 + " " + s2)

#45
s = "The quick brown fox jumps over the lazy dog"
t = s.split()
m = " "
print(m.join(t[::-1]))
