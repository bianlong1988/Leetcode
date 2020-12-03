#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution1:
    def find132pattern(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            temp_j = float('-inf')
            for j in range(i + 1, len(nums)):
                temp_k = nums[j]
                if nums[i] < nums[j]: #1<2
                    temp_j = max(temp_j,nums[j])  #temp_j = 4
                if nums[i]< temp_k < temp_j:
                    return True
        return False      

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_i = float('inf')
        stack, nums_i = [], []
        for i in range(n):
            min_i = min(min_i, nums[i])
            nums_i.append(min_i)
        
        for j in range(n - 1, -1, -1):
            # stack[-1] -> potential nums[K]
            # 4,[5,8]
            # i,k,j
            while stack and stack[-1] <= nums_i[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False
# @lc code=end

