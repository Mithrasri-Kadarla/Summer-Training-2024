'''l=list(map(int,input().split(' ')))
el=[]
ol=[]
for i in range(len(l)):
    if i%2==0:
        el.append(l[i])
elsum=sum(el)
olsum=sum(l)-elsum
print("If thief started from beginning:",olsum)
print("If thief started from 2nd House:",sum(l)-olsum)'''
def max_gold(houses):
    n = len(houses)
    if n == 0:
        return 0
    elif n == 1:
        return houses[0]
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):

        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[-1]
houses = [13, 9, 4, 10, 5, 7]
print("Maximum amount of gold stolen:", max_gold(houses))
