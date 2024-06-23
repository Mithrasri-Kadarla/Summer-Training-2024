'''def prim(graph):
    mst = []  
    visited_vertices = set() 
    start_vertex = list(graph.keys())[0] 

    visited_vertices.add(start_vertex)

    while len(visited_vertices) < len(graph):  
        min_weight = float('inf')
        min_edge = None

        for vertex in visited_vertices:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited_vertices and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)

        if min_edge:
            frm, to = min_edge
            mst.append((frm, to, graph[frm][to]))
            visited_vertices.add(to)

    return mst

graph = {
    5: {2: 2, 3: 2, 8: 2},
    2: {5: 2, 3: 1},
    3: {2: 1, 7: 3, 5: 2, 8: 3},
    7: {3: 3, 9: 1},
    8: {5: 2, 6: 4, 3: 3},
    6: {8: 4, 9: 2},
    4: {9: 2},
    9: {4: 2}
}

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree (Simple):", minimum_spanning_tree)
'''
graph = {
    5: {2: 2, 3: 2, 8: 2},
    2: {5: 2, 3: 1},
    3: {2: 1, 7: 3, 5: 2, 8: 3},
    7: {3: 3, 9: 1},
    8: {5: 2, 6: 4, 3: 3},
    6: {8: 4, 9: 2},
    4: {9: 2},
    9: {4: 2}
}

q = []
t = []
vi = [5]  

for neighbor, weight in graph[vi[-1]].items():
    q.append((vi[-1], neighbor, weight))

while q:
    q.sort(key=lambda x: x[-1])
    
    edge = q.pop(0)
    frm, to, weight = edge
    
    if to not in vi:
        vi.append(to)
        t.append(edge)
        
        for neighbor, weight in graph[to].items():
            if neighbor not in vi:
                q.append((to, neighbor, weight))

print("Minimum Spanning Tree (Edges):", t)






























