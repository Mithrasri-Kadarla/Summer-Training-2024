def add_even_with_odds(even, b, result=None):
    if result is None:
        result = []
    
    if not b:  # Base case: if list `b` is empty, return the result
        return result
    
    if b[0] % 2 != 0:  # If the current element of `b` is odd
        result.append(even + b[0])
    
    # Recur with the remaining elements of `b`
    return add_even_with_odds(even, b[1:], result)

def process_even_with_odds(a, b, result=None):
    if result is None:
        result = []
    
    if not a:  # Base case: if list `a` is empty, return the result
        return result
    
    if a[0] % 2 == 0:  # If the first element of `a` is even
        result = add_even_with_odds(a[0], b, result)
    
    # Recur with the remaining elements of `a`
    return process_even_with_odds(a[1:], b, result)

# Example usage:
a = [6, 3, 2, 9, 4, 7]
b = [8, 7, 5, 3, 6, 9]
result = process_even_with_odds(a, b)
print(result)  # Output the result
