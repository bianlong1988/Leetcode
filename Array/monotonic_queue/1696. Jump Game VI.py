class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # max{dp[i-k], dp[i-k+1]....dp[i-i]} + nums[i] => dp[i]:score
        #.     l                       r
        # sliding window
        
        n = len(nums)
        score = nums[0] # must include first & last score
        dq = collections.deque() # dq[i][0]: idx, dq[i][1]: score
        dq.append([0, nums[0]])
        for i in range(1, n):
            # popleft if len > k
            if dq and i - dq[0][0] > k:
                dq.popleft()
            # update max value in dq
            score = dq[0][1] + nums[i]
            # maintain decreasing dq 
            # 8 [7 7 6] xxxx
            while dq and dq[-1][1] <= score:
                dq.pop()
            dq.append([i, score])
        return score