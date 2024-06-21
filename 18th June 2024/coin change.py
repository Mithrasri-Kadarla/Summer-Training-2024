def coinChange(coins,amount):
    dp = [0] + [amount + 1] * amount  
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount]!=amount+1:
        return dp[amount]
    else:
        return -1
coins=[1,2,5]
amount=11
print(coinChange(coins,amount))
