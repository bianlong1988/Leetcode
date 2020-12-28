class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        return self.atMostK(A, K) - self.atMostK(A, K- 1)  # => exact K
    
    def atMostK(self, A, K):
        l = 0
        window = {}
        count = 0
        for r, char in enumerate(A):
            window[char] = window.get(char, 0) + 1
            while len(window) > K:
                window[A[l]] -= 1
                if window[A[l]] == 0:
                    del window[A[l]]
                l += 1
            # valid subArray
            count += r - l + 1
            
        return count 