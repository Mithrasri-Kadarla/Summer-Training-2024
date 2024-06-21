n='tu7gh7'
m='gg6gd7h1'
x=m+n
d=''
for i in x:
    if i.isdigit() and i not in d:
        d+=str(i)
print(d)
l=list(d)
l.sort()
l=l[::-1]
#print(l)
e=[]
o=[]
for i in l:
    if int(i)%2==0:
        e.append(int(i))
    elif int(i)%2!=0:
        o.append(int(i))
min_even=min(e)
min_odd=min(o)
l[-1]=str(min_even)
l[-2]=str(min_odd)
q=''
for i in l:
    q+=i
print(int(q))

