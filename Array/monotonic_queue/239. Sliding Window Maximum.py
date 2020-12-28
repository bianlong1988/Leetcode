class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = MQ()
        res = []
        l = 0
        for r, cur_num in enumerate(nums):
            dq.push(cur_num)
            if r - l + 1 == k:
                res.append(dq.max())
                if nums[l] == dq.max():
                    dq.pop()
                l += 1
        return res
    
#MonotonicQueue 
class MQ:
    def __init__(self):
        self.dq = collections.deque()
    def push(self, x):
        # push an element on the queue
        # pop all the elements smaller than x
        while self.dq and x > self.dq[-1]:
            self.dq.pop()
        self.dq.append(x)
        # print (self.dq)
    def pop(self):
        # pop the max element
        self.dq.popleft()
    def max(self):
        # return max element
        return self.dq[0]

        
        
        
        
    
                
                
                