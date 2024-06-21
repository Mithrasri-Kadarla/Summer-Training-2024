a=[1,2,3,5]
n=4
l=[]
for i in range(0,n+1):
    l.append(i)    
for i in range(1,n+1):
    for coin in a:
        if i>=coin:
            l[i]=min(l[i],l[i-coin]+1)
print(l[n])
