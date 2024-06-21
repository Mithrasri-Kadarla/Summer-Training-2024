def fun(i,j,k):
    if k==len(s):
        return 1
    if (i<0 or j<0 or i>=n or a[i][j]!=s[k]):
        return
    if (a[i][j]==s[k]):
        a[i][j]=0
    fun(i+1,j,k+1)
    fun(i-1,j,k+1)
    fun(i,j-1,k+1)
    fun(i,j+1,k+1)
    return t
for i in range(n):
    for j in range(n):
        if a[i][j]==s[0]:
            c=fun(i,j,1,0)
            if c==1:
                print("Yes")
                break
print("No")
