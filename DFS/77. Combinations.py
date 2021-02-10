class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, k, 1, res)
        return res
    
    def backtrack(self, n, k, start, res):
       #   1        2     3
       #  / | \    /\     /
       # 2  3 4   3 4    4
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            print (i)
            self.backtrack(n, k, i + 1, res)
            path.pop()