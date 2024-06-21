#number of islands

def no_islands(grid):
    c=0
    rows=len(grid)
    cols=len(grid[0])
    mx=0
    def dfs(i,j):
        if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]!="1":
            return 0
        grid[i][j]="0"
        a=1
        a+=dfs(i-1,j)
        a+=dfs(i+1,j)
        a+=dfs(i,j-1)
        a+=dfs(i,j+1)
        return a
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=="1":
                c+=1
                i_a=dfs(i,j)
                mx=max(mx,i_a)
    return c,mx
grid = [
  ["0","1","0","0","1"],
  ["1","0","0","1","1"],
  ["0","0","0","0","0"],
  ["1","0","0","0","0"],
  ["1","0","0","0","1"]
]
print(no_islands(grid))
