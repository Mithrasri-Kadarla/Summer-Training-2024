l=["school","car","apple","hi"]
l.sort(key=len)
print(l[::-1])
'''d={}
for i in l:
    d[len(i)]=i
x=sorted(d.items(),reverse=True)
print(x)'''
'''
b=[]
for i in l:
    b.append(len(i))
c=zip(b,l)
print(list(c))
c.sort()
for i,j in c:
    print(j)
'''
