a='abcd'
b='axbdc'
m=[]
for i in range(len(a)+1):
    l=[0]*(len(b)+1)
    m.append(l)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(a)][len(b)])
