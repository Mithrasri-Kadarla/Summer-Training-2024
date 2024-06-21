def nqueen(r):
    if r == n:
        return
    for c in range(n):
        if check(r, c):
            m[r][c] = 1
            break
    nqueen(r + 1)

def check(i, j):
    # Check if the position is in the same row or column as the rook
    if i == u or j == v:
        return False
    
    # Check the same column
    for row in range(i):
        if m[row][j] == 1:
            return False
    
    # Check the upper left diagonal
    row, col = i, j
    while row >= 0 and col >= 0:
        if m[row][col] == 1:
            return False
        row -= 1
        col -= 1
    
    # Check the upper right diagonal
    row, col = i, j
    while row >= 0 and col < n:
        if m[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True

n = 5
u = 1
v = 3
m = [[0] * n for _ in range(n)]
m[u][v] = 1  # Place the rook at (u, v)

nqueen(0)

# Print the board
for row in m:
    print(row)

# Calculate the sum of queens
sum_queens = sum(sum(row) for row in m) - 1  # Subtract 1 for the rook
print("Sum of queens:", sum_queens)
