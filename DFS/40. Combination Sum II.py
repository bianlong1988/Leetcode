class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []
        start = 0
        self.backtrack(candidates, target, res, path, start)
        return res

    def backtrack(self, candidates, target, res, path, start):
        #base condition
        if target < 0:
            return
        if target == 0:
            res.append(path[:])

        for i in range(start, len(candidates)):
            if i > start and candidates[i - 1] == candidates[i]:
                continue
            path.append(candidates[i])
            self.backtrack(candidates, target-candidates[i], res, path, i + 1)
            path.pop()