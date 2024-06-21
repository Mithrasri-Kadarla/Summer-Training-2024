a='abcd'
b='axbdc'
m=[]
s=''
for i in range(len(a)+1):
    l=[0]*(len(b)+1)
    m.append(l)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            m[i][j]=m[i-1][j-1]+1
            s+=a[i-1]
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(a)][len(b)])

s = ''
u= len(a)
v= len(b)
while(u>0 and v>0):  #or u!=0 and v!=0
    if(a[u-1]==b[v-1]):
        s=s+a[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u-1][v]>m[u][v-1]):
            u=u-1
        else:
            v=v-1
s=s[::-1]
print(s)
