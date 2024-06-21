def max_gold_recursive(h, i):
    if i < 0:
        return 0
    elif i == 0:
        return h[0]
    elif i == 1:
        return max(h[0], h[1])
    else:
        steal_current = h[i] + max_gold_recursive(h, i - 2)
        skip_current = max_gold_recursive(h, i - 1)
        return max(steal_current, skip_current)

def max_gold(h):
    return max_gold_recursive(h, len(h) - 1)

h = [13, 9, 4, 10, 5, 7]
print("Maximum amount of gold stolen:", max_gold(h))
'''
                                    [13,9,4,10,5,7]
                                       /        \
                                13[4,10,5,7]   9[10,5,7]
                                    /   \        /     \
                                4[5,7] 10[7]   10[7]  5[]
                                 / \    / \     / \
                                5[] 7[] 7[]    7[]
 

'''
