arr=[4,3,4,5,6,1,0,6,7]
n=len(arr)
l=[]
r=[]
x=0
for i in range(1,n-1):
    l=max(arr[:i])
    r=max(arr[i+1:])
    x+=max(0,min(l,r)-arr[i])

print(x)
