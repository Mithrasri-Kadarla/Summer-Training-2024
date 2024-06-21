def find_min_cost_path(d, start, end, visited=None, path=None, current_cost=0, min_cost=float('inf'), min_path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == end:
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = path[:]
    else:
        for neighbor, cost in d.get(start, []):
            if neighbor not in visited:
                new_visited = visited.copy()
                new_path = path.copy()
                result_path, result_cost = find_min_cost_path(d, neighbor, end, new_visited, new_path, current_cost + cost, min_cost, min_path)
                if result_cost < min_cost:
                    min_cost = result_cost
                    min_path = result_path

    path.pop()
    visited.remove(start)
    return min_path, min_cost

# Define the graph
d = {
    5: [[7, 1], [3, 2]],
    7: [[5, 1], [4, 2], [3, 3]],
    4: [[7, 2], [8, 2], [2, 2]],
    8: [[3, 1], [4, 2], [2, 3]],
    3: [[5, 2], [7, 3], [8, 1]],
    2: [[4, 4], [8, 3]]
}

# Find the minimum cost path from node 5 to node 2
start_node = 5
end_node = 2
min_path, min_cost = find_min_cost_path(d, start_node, end_node)

# Print the results
print("Minimum cost path:", min_path)
print("Minimum cost:", min_cost)
