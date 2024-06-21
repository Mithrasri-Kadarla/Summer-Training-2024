def paths(m,n):
    if m==1 and n==2:## This is obstacle
        return 0
    elif m==1 or n==1:
        return 1
    elif m==0 or n==0:
        return 0
    
    else:
        return paths(m-1,n)+paths(m,n-1)
print(paths(4,3))
