def diedai(coins, amount):
    dp = [-1]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0 and dp[i-coin] != -1:
                if dp[i] == -1 or dp[i] > dp[i-coin] + 1:
                    dp[i] = dp[i-coin] + 1
    print(dp)
    return dp[amount]

min_coins = diedai([1, 2, 5, 7, 10], 14)
print(min_coins)
