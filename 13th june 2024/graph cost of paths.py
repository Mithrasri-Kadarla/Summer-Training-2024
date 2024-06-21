def fun(d, x, e, c, l):
    l.append(x)  # Append the current node to the path list
    if x == e:   # Check if the current node is the end node
        print(l, c)
        l.pop()
        return c
    for i in d.get(x, []):  # Get neighbors of the current node
        if i[0] not in l:  # Check if the neighbor is not in the path
            fun(d, i[0], e, c + i[1], l)  # Recursive call with updated cost and path
    l.pop()
    return None

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
