def fun(i,j,c):
    if i>0 or i>=n or j<0 or j>=m:
        return
    if i==m-1 and j==n-1:
        c+=1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,c)
    if((i,j-1)not in vi):
        c=fun(i,j-1,c)
    if((i+1,j) not in vi):
        c=fun(i+1,j,c)
    if((i,j+1)not in vi):
        c=fun(i,j+1,c)
    vi.pop()
    return c
print(fun(3,3,0))
