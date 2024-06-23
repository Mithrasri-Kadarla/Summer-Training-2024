def fun(x):
    return x[1]
a=[[3,5],[7,1],[2,8],[9,3],[5,6]]
a.sort(key=fun)
print(a)
