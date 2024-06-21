def fun(lst1, lst2):
    res=[] 
    if not lst1:
        return res
    def recur(i,j):
        if lst1[i]%2==0 and lst2[i]%2!=0:
            res.append(lst1[i]+lst2[j])
        elif lst1[i]%2!=0:
            if i<len(lst1)-1:
                recur(i+1,j)
        else:
            if j<len(lst2)-1:
                recur(i,j+1)
    recur(0,0)
    return res
     
lst1=[6,3,2,9,4,7]
lst2=[8,7,5,3,6,9]
print(fun(lst1,lst2))
