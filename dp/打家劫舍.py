
def diedai(nums):
    if not nums:
        return 0
    dp = []
    dp.extend([nums[0], max(nums[0], nums[1])])
    i = 1
    while i < len(nums)-1:
        i += 1
        dp.append(max(dp[i-1], dp[i-2] + nums[i]))
        print(i)
        print(dp)
    return dp[i]

max_money = diedai([5,2,6,3,1,7])
print(max_money)
