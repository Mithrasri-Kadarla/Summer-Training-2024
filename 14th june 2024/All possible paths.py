def f_paths(d,start,end,path):
    path=path+[start]
    if start==end:
        return [path]
    if start not in d:
        return []
    paths=[]
    for node in d[start]:
        if node not in path:
            nxt=f_paths(d,node,end,path)
            for i in nxt:
                paths.append(i)
    return paths
x=f_paths(d,5,2,[])
for path in x:
    print(path)
