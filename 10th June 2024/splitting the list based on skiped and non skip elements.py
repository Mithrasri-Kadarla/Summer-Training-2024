# input:               4 5 2 1                  1 2 3 4 1 2 3 1 2                          2 3 1 3 4 3 2
#output:            [[4, 5, 2, 1]]          [[1, 2, 3, 4], [1, 2, 3], [1, 2]]           [[2, 3, 1, 4], [3, 2], [3]]

def split(l):
    res = []
    non_skip = []
    skip = []
    seen = set() 
    for i in l:
        if i not in seen:
            non_skip.append(i)
            seen.add(i)
        else:
            skip.append(i)
    
    res.append(non_skip)
    
    if skip:  
        res.extend(split(skip))
    
    return res

l = list(map(int, input().split()))  
result = split(l)
print(result)
