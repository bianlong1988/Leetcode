#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return i == len(popped)
        
# @lc code=end

