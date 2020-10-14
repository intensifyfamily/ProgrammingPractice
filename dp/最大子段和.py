def diedai(nums):
    if not nums:
        return 0
    dp = []
    dp.append(nums[0])
    i = 0
    max_money = dp[0]
    while i < len(nums)-1:
        i += 1
        dp.append(max(nums[i], dp[i-1]+nums[i]))
        if dp[i] > max_money:
            max_money = dp[i]
    return max_money

max_child_sum = diedai([-2,1,-3,4,-1,2,1,-5,4])
print(max_child_sum)
