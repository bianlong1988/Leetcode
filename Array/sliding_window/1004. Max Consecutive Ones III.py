class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """
        [1,1,1,0,0,0,1,1,1,1,0]
         0 1 2 3 4 5 6 7 8 9 10
         l 
                 r
               k k 
        """
        l = 0
        zeros = 0 # zeros in the window
        max_len = float('-inf')
        for r in range(len(A)):
            if A[r] == 0:
                zeros += 1
            while zeros > K: # not valid
                if A[l] == 0:
                    zeros -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

            
        return 0 if max_len == float('-inf') else max_len