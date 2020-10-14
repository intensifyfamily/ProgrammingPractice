def diedai(grid):
    if not grid:
        return 0
    row = len(grid)
    column = len(grid[0])
    dp = [[0] * len(g) for g in grid]
    dp[0][0] = grid[0][0]
    for i in range(1, column):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for j in range(1, row):
        dp[j][0] = grid[j-1][0] + grid[j][0]
        for k in range(1, column):
            dp[j][k] = min(dp[j-1][k], dp[j][k-1]) + grid[j][k]

    return dp[row-1][column-1]

min_path_sum = diedai([
                        [1,3,1],
                        [1,5,1],
                        [4,2,1]
                      ]
                    )
print(min_path_sum)

