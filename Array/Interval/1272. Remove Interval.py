class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        """
        1. |    |
              |.   |
        2.     |.  |
            |.   |
        3. |      |
              |. |
        4.    |. |
            |.      |
        5.                |.   |
             |         |          |         |
        
        """
        res = []
        for idx, i in enumerate(intervals):
            if i[0] > toBeRemoved[1] or i[1] < toBeRemoved[0]:
                res.append(i)
            else:
                if i[0] < toBeRemoved[0]:
                    res.append([i[0], toBeRemoved[0]])
                if i[1] > toBeRemoved[1]:
                    res.append([toBeRemoved[1], i[1]])
                            
        return res