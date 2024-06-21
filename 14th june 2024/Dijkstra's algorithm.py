d={5:[(7,1),(3,2)],7:[(5,1) ,(4,2),(3,8)],4:[(7,2),(8,9),(2,7)],8:[(3,4),(4,9),(2,6)],3:[(5,3),(7,8),(8,4)],2:[(4,7),(8,6)]}

def dj(d,start):
    visi=set()
    dis={node:float('inf') for node in d}
    dis[start]=0
    queue=[(0,start)]
    while queue:
        c,node=min(queue)
        queue.remove((c,node))
        if node not in visi:
            visi.add(node)
            print(node)
            if node in d:
                for nei,wt in d[node]:
                    if dis[node]+wt<dis[nei]:
                        dis[nei]=dis[node]+wt
                        queue.append((dis[nei],nei))
    return dis

dj(d,5)
