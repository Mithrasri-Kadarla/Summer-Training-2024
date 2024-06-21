def unique_paths_with_paths(m, n):
    def dfs(x, y, visited, path, all_paths):
        if x == m - 1 and y == n - 1:
            all_paths.append(path[:])
            return
        
        visited.add((x, y))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                path.append((nx, ny))
                dfs(nx, ny, visited, path, all_paths)
                path.pop()
        
        visited.remove((x, y))
    
    if m == 0 or n == 0:
        return 0, []
    
    all_paths = []
    dfs(0, 0, set(), [(0, 0)], all_paths)
    
    return len(all_paths), all_paths

# Example usage:
num_paths, paths = unique_paths_with_paths(2,3)
print(f"Number of unique paths: {num_paths}")
print("Paths:")
for path in paths:
    print(path)
