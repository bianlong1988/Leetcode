class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        """
        Hashmap + Prefix sum
        prefix[i - 1] = prefix[j] - S
        """
        # key: prefix sum; value: count of the sum
        prefix_sum = {0:1} 
        # 0[1,0,1,0] S=2
        #   i.    j  
        prefix = 0
        res = 0

        for j in range(len(A)):
            prefix += A[j]
            if prefix - S in prefix_sum:
                res += prefix_sum[prefix - S]
            prefix_sum[prefix] = prefix_sum.get(prefix, 0) + 1
            
        return res
                
            
            
        
        
        