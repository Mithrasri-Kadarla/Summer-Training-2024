d={1:[7,3,4],7:[1,6],6:[3,5,2],3:[1,6,4],5:[4,6,2],2:[5,6],4:[1,3,5]}
#d ={5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8:[3, 4, 2],3:[5, 7, 8], 2: [4, 8]}
def bfs(d,n):
    v=[]
    q=[n]
    while(q):
        for i in d[q[0]]:   #d[n] or d[q[0]]
            if(i not in q and i not in v):
                q.append(i)
        v.append(q.pop(0))
        print(v[-1],end=" ")
bfs(d,1)

        
        
