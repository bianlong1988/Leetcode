class Solution:
  
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
       [2,3,1,2,4,3]
        l
              r
        window = r - l + 1
       """     
        min_len = float('inf')
        w_sum = 0
        l = 0
        for r in range(len(nums)):
            w_sum += nums[r]
            while w_sum >= s:
                min_len = min(min_len, r - l + 1)
                w_sum -= nums[l]
                l += 1
        return 0 if min_len == float('inf') else min_len
                
            
            
            
  
            
            
            
        
                