class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        A[i] ~ max subset sum of nums[0~i] and nums[i] is selected
        1. A[i] = max{A[i-1], A[i-2]....A[i-k], 0} + nums[i]
                   dq[i -k ,  ,   ...                 i]
        2. window lengh: i -k >= 0
            0: means use nums[i] itself, not include previous sum
        """
        A = [0] * len(nums)
        max_len = 0
        dq = collections.deque() # decreasing deque holds sum
        for i in range(len(nums)):
            # A[i] = max{A[i-1], A[i-2]....A[i-k], 0} + A[i]
            A[i] = max(Adq[0], 0) + nums[i] if dq else 0
            print ('A',A)
            
            # pop to maintain deacresing deque
            while dq and A[i] > nums[dq[-1]]:
                dq.pop()
            # update dq
            dq.append(i)
            print ('dq', dq)
            # popleft if the window is not valid
            # dq[0] == A[i - k] means can only popleft the element 
            # if it hasn't been removed yet at the corresponding index
            if i >= k and dq and dq[0] <= i - k:
                dq.popleft()
            max_len = max(max_len, A[i])
        return max_len
    

            

                

                
            