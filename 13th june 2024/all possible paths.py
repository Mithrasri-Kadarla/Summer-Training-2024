def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:  
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

d = {
    5: [7, 3],
    7: [5, 4, 3],
    4: [7, 8, 2],
    8: [3, 4, 2],
    3: [5, 7, 8],
    2: [4, 8]
}

paths = find_all_paths(d, 5, 2)
for path in paths:
    print(path)
