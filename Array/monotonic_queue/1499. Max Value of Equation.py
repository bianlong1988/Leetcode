class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
         1. maximum value of the equation yi + yj + |xi - xj|
         => for each j look for valid i => yj + xj + max{-xi + yi}, 
         
         2. xj - xi <= k
         x: points[][0], y: points[][1]
         i: dq[0], j
         [8765] j
        """
        dq = collections.deque()
        max_val = float('-inf')
        for j in range(len(points)):
            # popleft if NOT xj - xi <= k:
            while dq and points[j][0] - points[dq[0]][0] > k:
                dq.popleft()
                
            if dq:    
                max_val = max(points[j][1] + points[j][0] - points[dq[0]][0] + points[dq[0]][1], max_val)
            
            # pop to maintain decreasing deque
            while dq and -points[dq[-1]][0] + points[dq[-1]][1] < -points[j][0] + points[j][1]:
                dq.pop()
            dq.append(j)
            
        return max_val