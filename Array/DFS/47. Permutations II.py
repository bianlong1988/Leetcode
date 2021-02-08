class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        visited = [False] * len(nums)
        self.backtrack(nums, [], res, visited)
        return res
    
    def backtrack(self, nums, path, res, visited):
        
        if len(path) == len(nums):
            res.append(path)
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i - 1] == nums[i] and visited[i - 1]:
                continue
            else:
                visited[i] = True
                path.append(nums[i])
                self.backtrack(nums, path[:], res, visited)
                path.pop()
                visited[i] = False