def fun(d, start, visited=[]):
    if start not in visited:
        visited.append(start)
        for i in d.get(start, []):
            fun(d, i, visited)
    return visited

d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
visited_nodes = fun(d, 5)
print(visited_nodes)
