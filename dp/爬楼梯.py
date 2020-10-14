import timeit


def digui(n):
    if n == 1 or n==2:
        return n
    return digui(n-1) + digui(n-2)
print(digui(20))

def diedai(n):
    dp = []
    dp.extend([0, 1, 2])
    i = 2
    while i < n:
        i += 1
        dp.append(dp[i-1] + dp[i-2])
    return dp[i]

print(diedai(20))

