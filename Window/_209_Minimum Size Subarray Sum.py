
"""
Option one: Nested loops
    Time O(n^2), Space O(n)
Option two: Binary Search
    To be continued....
Option tree: Two Pointers
    Time O(n), Space O(n\1)
"""
"""
1. Nested loops
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')

        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum = nums[j] + sum
                if sum >= s:
                    ans = min(ans, j - i + 1)
                    break

        return 0 if ans == float('inf') else ans

"""
3. Tow pointers:
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            while sum >= s:
                ans = min(ans, i + 1 - left)
                sum = sum - nums[left]
                left = left + 1
        return 0 if ans == float('inf') else ans
