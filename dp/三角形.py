def diedai(triangle):
    if not triangle:
        return 0
    dp = [[0] * len(t) for t in triangle]
    dp[-1] = triangle[-1]
    for i in range(len(dp)-2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    return dp[0][0]
min_dis = diedai([[2],[3,4],[6,5,7],[4,1,8,3]])
print(min_dis)

