def can_make_target(l, t, current_sum=0, index=0):

    if current_sum == t:
        return True
    if index >= len(l) or current_sum > t:
        return False
    if can_make_target(l,t,current_sum+l[index],index+1):
        return True
    if can_make_target(l, t, current_sum, index + 1):
        return True
    return False
l = [2, 3, 5, 6]
t = 11

if can_make_target(l, t):
    print("Yes")
else:
    print("No")
