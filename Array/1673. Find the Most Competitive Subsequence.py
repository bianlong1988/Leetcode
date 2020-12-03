class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for idx, cur_num in enumerate(nums):
            while stack and stack[-1] > cur_num and len(stack) + (n - idx - 1) >= k :
                stack.pop()
            if len(stack) < k:   
                stack.append(cur_num)

            # print (stack)
        return stack