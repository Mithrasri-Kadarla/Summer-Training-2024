def recur(x):
    if x==0:
        return 0
    return x+recur(x-2)
n=10
if n%2==0:
    print(recur(n))
else:
    print(recur(n-1))
