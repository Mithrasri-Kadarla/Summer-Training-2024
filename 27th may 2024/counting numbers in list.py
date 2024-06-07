x=list(map(int,input().split(' ')))#3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
d={}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i, j in d.items():
    print(i,'-' ,j)
print('________________________________________________')
a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,'-',a.count(i))
