def is_valid_move(x, y, rows, cols):
    """ Check if the move is within the bounds of the matrix """
    return 0 <= x < rows and 0 <= y < cols

def search_from_cell(grid, word, row, col, index):
    """ Recursive function to search the word from a specific cell """
    if index == len(word):
        return True
    
    if not is_valid_move(row, col, len(grid), len(grid[0])) or grid[row][col] != word[index]:
        return False
    
    # Temporarily mark the current cell to avoid revisiting
    temp = grid[row][col]
    grid[row][col] = '#'
    
    # Explore 4 possible directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        if search_from_cell(grid, word, row + dx, col + dy, index + 1):
            grid[row][col] = temp  # Restore the cell's original value
            return True
    
    grid[row][col] = temp  # Restore the cell's original value
    return False

def search_word(grid, word):
    """ Main function to search for the word in the 2D list """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if search_from_cell(grid, word, row, col, 0):
                return True
    return False

# Test the function
grid = [
    ['c','s','v','r'],
    ['x','w','v','s'],
    ['r','o','a','d'],
    ['d','e','a','n']
]
word = input("Enter the word to search: ")
print(search_word(grid, word))
