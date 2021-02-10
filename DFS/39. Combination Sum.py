class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(candidates, target, [], res, 0)
        return res
    
    def backtrack(self, candidates, target, path, res, start):
        if sum(path) > target:
            return
        if sum(path) == target:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.backtrack(candidates, target, path, res, i)
            path.pop()