class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        prefix_sum = [0]
        for x in A:
            prefix_sum.append(prefix_sum[-1] + x)           
        dq = collections.deque()
        min_len = float('inf')
        for r, cur_sum in enumerate(prefix_sum):
            # if last elenment in deque is less equal to the current number
            # e.g. dq[-1] > cur_sum => if dq[-1] is valid, cur_sum will be valid and shorter
            # -> thus, this dq is a increasing deque
            while dq and prefix_sum[dq[-1]] >= cur_sum:
                dq.pop()
            
            # prefix[r] - prefix[l] >= K
            # while valid window => shrink & update => shortest
            while dq and prefix_sum[r] - prefix_sum[dq[0]] >= K:
                l = dq.popleft()
                min_len = min(min_len, r - l)
            dq.append(r)
        return -1 if min_len == float('inf') else min_len