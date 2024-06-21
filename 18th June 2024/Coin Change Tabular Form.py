def coin_change(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  

    for coin in coins:
        for amount in range(coin, target + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[target] if dp[target] != float('inf') else -1

coins = [3, 4]
target = 6
min_coins = coin_change(coins, target)
print(min_coins)
