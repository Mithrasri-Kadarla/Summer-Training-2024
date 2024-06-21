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
l=[3,5,9,6,8,10]
#l = [4,3,4,5,6,1,0,6,7]
x=fun(l)
print("From left:",list(set(x)))
s = l[::-1]
y=fun(s)
y=y[::-1]
print('From Right:',list(set(y)))
res=0
for i in range(len(l)):
    res+=min(x[i],y[i])-l[i]
print(res)
