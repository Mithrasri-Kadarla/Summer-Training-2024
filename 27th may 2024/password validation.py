x=input()
l=0
u=0
d=0
s=0
r=[]
for i in x:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i.isdigit():
        d+=1
    elif (not i.isalnum()):
        s+=1
r.append(l)
r.append(u)
r.append(d)
r.append(s)
print(r)
c=0
if len(x)>=0:
    
    if r[0] is 0:
        c+=1
    if r[1] is 0:
        c+=1
    if r[2] is 0:
        c+=1
    if r[3] is 0:
        c+=1
print(c)
if all(r):
    print(-1)
    


