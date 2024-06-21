n=int(input())
l=[]
def prefix(l,n):
    c=0
    for i in set(l):
        if n in i:
            c+=1       
    return c
for i in range(n):
    m,n=input().split(' ')
    if m=='1' and n not in l:
        l.append(n)
    elif m=='2':
        if n in l:
            print("True")
        else:
            print("False")
    elif m=='3':
        print(prefix(l,n))
    elif m=='4':
        s=set(l)
        l=list(s)
        l.remove(n)
    
