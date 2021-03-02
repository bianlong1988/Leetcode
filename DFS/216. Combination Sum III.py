class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(k, n, [], res, 1)
        return res
    
    def dfs(self, k, n, path, res, start):
        # base case
        if k == 0 and n == 0:
            res.append(path[:])
            return
        if n < 0:
            return
        
        for i in range(start, 10):
            path.append(i)
            self.dfs(k - 1, n - i, path, res, i + 1)
            path.pop()