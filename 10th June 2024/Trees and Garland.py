'''6
0 1 1 1 0 1
0 1 0 1 0 0
1 0 1 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 1 0
4 6'''
n = 6
forest =[[0,1,1,1,0,1],
         [0,1,0,1,0,0],
         [1,0,1,1,0,0],
         [0,0,0,1,1,1],
         [1,1,0,0,0,1],
         [1,1,1,0,1,0]] 

start_row, start_col = map(int, input().split())

# Directions for moving up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

def burn_trees(forest, start_row, start_col):
    if forest[start_row][start_col] == 0:
        return
    
    queue = [(start_row, start_col)]
    forest[start_row][start_col] = 0  
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and forest[nx][ny] == 1:
                forest[nx][ny] = 0  
                queue.append((nx, ny))

burn_trees(forest, start_row - 1, start_col - 1)  

remaining_trees = sum(row.count(1) for row in forest)
print(remaining_trees)
