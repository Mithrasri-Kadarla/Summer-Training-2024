def print_pattern():
    n = 3 
    m = 5  
    
    for i in range(m):
        for j in range(m):
            if i == 0 or i == m-1: 
                print("*", end=" ")
            elif j == 0 or j == m-1:  
                print("*", end=" ")
            else:
                print((i-1) * n + j, end=" ")
        print()


print_pattern()
