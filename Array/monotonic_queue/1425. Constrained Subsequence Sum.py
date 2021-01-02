class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        A[i] ~ max subset sum of nums[0~i] and A[i] is selected
        1. A[i] = max{A[i-1], A[i-2]....A[i-k], 0} + A[i]
        2. window lengh: i -k >= 0
            0: means use nums[i] itself, not include previous sum
        """
        A = nums[:]
        dq = collections.deque() # decreasing deque holds sum
        for i in range(len(nums)):
            # A[i] = max{A[i-1], A[i-2]....A[i-k], 0} + A[i]
            A[i] += dq[0] if dq else 0
            
            # pop to maintain deacresing deque
            while dq and A[i] > dq[-1]:
                dq.pop()
            # update dq, negtive value will not be added to dq, 
            # nums[i] it self will become the new max sum
            if A[i] > 0:
                dq.append(A[i])
            # popleft if the window is not valid
            # dq[0] == A[i - k] means can only popleft the element 
            # if it hasn't been removed yet at the corresponding index
            if i >= k and dq and dq[0] == A[i - k]:
                dq.popleft()
        return max(A)