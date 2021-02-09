class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        1,2,3
        1     2      3    
      2 3 2   3    
          3    
        """
        res, path, start = [], [], 0
        self.backtrack(nums, path, res, start)
        return res

    def backtrack(self, nums, path, res, start):
        # base condition
        res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, path, res, i + 1)
            path.pop()