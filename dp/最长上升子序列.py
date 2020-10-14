def diedai(nums):
    if not nums:
        return 0
    dp = [0] * len(nums)
    dp[0] = 1
    LIS = 1
    for i in range(1, len(dp)):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        if LIS < dp[i]:
            LIS = dp[i]
    return LIS

lis = diedai([1,2,3,2,1,4])
print(lis)
