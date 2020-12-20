class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        0 [1, -1, 5, -2, 3]
        -1
        """
        prefix_sum = {0:-1} # include the situation where [0:i]is valid
        cur_sum = 0
        max_len = 0
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = i
            if cur_sum - k in prefix_sum:
                # print (i, cur_sum, prefix_sum)
                max_len = max(i - prefix_sum[cur_sum - k], max_len)
        return max_len