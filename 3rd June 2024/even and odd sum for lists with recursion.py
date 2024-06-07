#using recusrion print sum of even numbers in a list  and odd numbers b list
def fun(i, s1, s2, lst):
    if i == len(lst):
        return s1, s2
    if lst[i] % 2 == 0:
        s1 += lst[i]
    else:
        s2 += lst[i]
    return fun(i + 1, s1, s2, lst)

a = [4, 6, 2, 1, 0]
b = [5, 1, 7, 96, 1]

even_sum_a, odd_sum_a = fun(0, 0, 0, a)
even_sum_b, odd_sum_b = fun(0, 0, 0, b)

print("Sum of even numbers in list a:", even_sum_a)
print("Sum of odd numbers in list a:", odd_sum_a)
print("Sum of even numbers in list b:", even_sum_b)
print("Sum of odd numbers in list b:", odd_sum_b)
