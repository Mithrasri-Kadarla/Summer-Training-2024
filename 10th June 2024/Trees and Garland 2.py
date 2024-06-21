def trees(grid,row,col):
    rows=len(grid)
    cols=len(grid[0])
    if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]==0:
        return    
    grid[row][col]=0
    trees(grid,row-1,col)  
    trees(grid,row+1,col) 
    trees(grid,row,col-1)  
    trees(grid,row,col+1)  
def rem(grid):
    c=0
    for row in grid:
        c+=sum(row)
    return c
grid=[[0,1,1,1,0,1],
      [0,1,0,1,0,0],
      [1,0,1,1,0,0],
      [0,0,0,1,1,1],
      [1,1,0,0,0,1],
      [1,1,1,0,1,0]]    
row=4
col=6
trees(grid,row-1,col-1)
print(rem(grid))
