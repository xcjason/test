def longestIncreament(nums):
	dp = [0] * len(nums)
	for i in xrange(len(nums)):
		for j in xrange(i):
			if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j])
		dp[i] += 1
	return max(dp)

L = [7, 2, 3, 1, 5, 8, 9, 6]
print longestIncreament(L)