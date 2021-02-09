class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.backtrack(nums, [], res, 0)
        return res
    
    def backtrack(self, nums, path, res, start):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i] :
                continue
                
            path.append(nums[i])
            self.backtrack(nums, path, res, i + 1)
            path.pop()
            