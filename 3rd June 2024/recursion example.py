def fun(x):
    if x==3:
        return 500
    print(x)
    t=fun(x+1)
    print(t)
    print(x)
print(fun(1))
