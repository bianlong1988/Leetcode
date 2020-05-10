"""
The Dutch National Flag Problem (The Quicksort "Band-Aid")
Option 1:
    tow pass:
        forward scan + backward scan
Option 2:
    ...
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[j], nums[i] = nums[i], nums[j]
                j = j + 1

        n = len(nums) - 1
        for m in range(len(nums) - 1, j - 1, -1):
            if nums[m] > 1:
                nums[m], nums[n] = nums[n], nums[m]
                n = n - 1
