class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1.
               |  |    |   |
          |  |
        2.  
            |  |    |   |
                |  |
        3. 
            merge
        """
        res = []
        # intervals.sort(key:lambda x:x[0])
        
        for idx, i in enumerate(intervals):
            start, end = i[0], i[-1]
            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[idx:]
            elif end < newInterval[0]:
                res.append(i)
            else:            
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])

        res.append(newInterval)    
        return res
                
                