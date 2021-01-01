class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dq_min, dq_max = collections.deque(), collections.deque()
        l = 0
        res = 0
        for r in range(len(nums)):
            # increasing deque [1234]3
            while dq_min and nums[dq_min[-1]] > nums[r]:
                dq_min.pop()
            # increasing deque [54321]3
            while dq_max and nums[dq_max[-1]] < nums[r]:
                dq_max.pop()
                
            dq_min.append(r)
            dq_max.append(r)
            
            while nums[dq_max[0]] - nums[dq_min[0]] > limit: # invalid window
                #index <= l will be removed
                if dq_max[0] <= l:
                    dq_max.popleft()
                if dq_min[0] <= l:
                    dq_min.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res