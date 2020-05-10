"""
1. brute force
"""

# class Solution(object):
#     def maxSubArrayLen(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         size = 0
#
#         for i in range(len(nums)):
#             sum = 0  # reset at every i
#             for j in range(i, len(nums)):
#                 sum = sum + nums[j]
#                 if sum == k:
#                     size = max(size, j - i + 1)
#
#         return  size if size != 0 else 0
"""
2. Prefix Sum
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = 0
        dic = {0: -1}
        sum = 0
        for j in range(len(nums)):
            sum = sum + nums[j]
            if (sum - k) in dic:
                size = max(size, j - dic[sum - k])
            if sum not in dic:
                dic[sum] = j
        return size


solution = Solution()
print solution.maxSubArrayLen([-2, -1, 2, 1], 1)
