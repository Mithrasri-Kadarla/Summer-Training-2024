def fun(d, x, e, c, m,l1):
    l.append(x)
    if x==e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=fun(d,i[0],e,c+i[0])
    

d = {
    5: [[7, 1], [3, 2]],
    7: [[5, 1], [4, 2], [3, 3]],
    4: [[7, 2], [8, 2], [2, 2]],
    8: [[3, 1], [4, 2], [2, 3]],
    3: [[5, 2], [7, 3], [8, 1]],
    2: [[4, 4], [8, 3]]
}
l = []
print(fun(d, 5, 2, 0, l))
