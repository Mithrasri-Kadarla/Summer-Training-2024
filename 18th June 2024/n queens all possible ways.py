class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        lst=[]
        v_cols=set()
        v_diag=set()
        v_diag2=set()
        def backtrack(row):
            if row==n:
                lst.append(["".join(i) for i in board])
                return
            for col in range(n):
                bd=row-col
                fd=row+col
                if not (col in v_cols or bd in v_diag or fd in v_diag2):
                    v_cols.add(col)
                    v_diag.add(bd)
                    v_diag2.add(fd)
                    board[row][col]="Q"
                    backtrack(row+1)
                    v_cols.remove(col)
                    v_diag.remove(bd)
                    v_diag2.remove(fd)
                    board[row][col]="."
            backtrack(0)
        return lst
