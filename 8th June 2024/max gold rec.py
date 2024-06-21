def mx_gold(arr):
    d={}
    def recur(i,d):
        if i<0:
            return 0
        if i==0:
            return arr[0]
        if i in d:
            return d[i]
        rob=arr[i]+recur(i-2,d)
        skp=recur(i-1,d)
        d[i]=max(rob,skp)
        return d[i]
     
    return recur(len(arr)-1,d)
arr=[13,9,4,10,5,7]
print(mx_gold(arr))
