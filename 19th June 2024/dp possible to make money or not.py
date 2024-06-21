l=[2,3,5,6]
t=11
def can_make_target_with_dp(l, t):
    dp = [False] * (t + 1)
    
    dp[0] = True
    
    for coin in l:
        for i in range(t, coin - 1, -1):
            if dp[i - coin]:
                dp[i] = True
    
    return dp[t]

l = [2, 3, 5, 6]
t = 12

if can_make_target_with_dp(l, t):
    print("Yes")
else:
    print("No")
