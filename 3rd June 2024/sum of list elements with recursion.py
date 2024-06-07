def fun(x,s):
    if x==len(a):
        return s
    s+=a[x]
    return fun(x+1,s)
a=[7,6,1]
print(fun(0,0))
