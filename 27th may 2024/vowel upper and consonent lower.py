s=input()
v=['a','e','i','o','u']
x=''
for i in s:
    if i not in v:
        x+=i.lower()
    elif i in v and i.islower():
        x+=i.upper()
print(x)
