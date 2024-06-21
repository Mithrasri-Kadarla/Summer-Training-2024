def fun(l):
    x = []
    for i in range(len(l)):
        if i == 0:
            x.append(l[i])
        else:
            if l[i] > x[i-1]:
                x.append(l[i])
            else:
                x.append(x[i-1])
    return x
#l=[2,5,2,3,6,7,1,0,5,7]
l = [4,3,4,5,6,1,0,6,7]
x=fun(l)

s = l[::-1]
y=fun(s)
y=y[::-1]
res=0
for i in range(len(l)):
    res+=min(x[i],y[i])-l[i]
print(res)
