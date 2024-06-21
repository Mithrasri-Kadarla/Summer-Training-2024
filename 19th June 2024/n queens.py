def solve_n_queens(n):
    def create_board(n):
        return [[0 for _ in range(n)] for _ in range(n)]

    def is_safe(board, row, col):
        i = 0
        while i < col:
            if board[row][i] == 1:
                return False
            i += 1

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solve(board, col, n):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1, n):
                    return True
                board[i][col] = 0
        return False

    board = create_board(n)
    if not solve(board, 0, n):
        return [], 0
    return board, sum(sum(row) for row in board)

solution, num_queens = solve_n_queens(4)
for row in solution:
    print(row)
print("Number of queens:", num_queens)
