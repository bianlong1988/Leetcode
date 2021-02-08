class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(nums, [], res)
        return res
    
    def backtrack(self, nums, path, res):
        
        if len(path) == len(nums):
            res.append(path)
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                self.backtrack(nums, path[:], res)
                path.pop()
                