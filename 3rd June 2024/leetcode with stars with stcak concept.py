s = "leet**cod*e"
l = []

for i in s:
    if i != '*':
        l.append(i)
    else:
        if l: 
            l.pop(-1)

x = ''.join(l)
print(x)
