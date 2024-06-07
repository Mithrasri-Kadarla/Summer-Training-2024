def e_sum(lst, n):
    if n == 0:
        return 0
    if lst[n-1] % 2 == 0:
        return lst[n-1] + e_sum(lst, n-1)
    else:
        return e_sum(lst, n-1)

def o_sum(lst, n):
    if n == 0:
        return 0
    if lst[n-1] % 2 != 0:
        return lst[n-1] + o_sum(lst, n-1)
    else:
        return o_sum(lst, n-1)

a = [3, 8, 5, 4, 3]
b = [5, 0, 9, 3, 2]
print(e_sum(a, len(a)))
print(o_sum(a, len(a)))
print(e_sum(b, len(b)))
print(o_sum(b, len(b)))
