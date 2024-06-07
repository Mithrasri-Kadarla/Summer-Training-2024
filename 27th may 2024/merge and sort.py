l1=list(map(int,input().split(' ')))
l2=list(map(int,input().split(' ')))
def sort_function(l1,l2):
    i=0
    j=0
    c=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            c.append(l1[i])
            i+=1
        else:
            c.append(l2[j])
            j+=1
    while i<len(l1):
        c.append(l1[i])
        i+=1
    while j<len(l2):
        c.append(l2[j])
        j+=1
    return c
print(sort_function(l1,l2))
