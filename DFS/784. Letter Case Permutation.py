class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.dfs(S, [], res, 0)
        return res

    def dfs(self, S, path, res, start):
        # base
        if len(path) == len(S):
            res.append("".join(path[:]))
            return
        # backtrack
        for i in range(start, len(S)):
            cur_char = S[i]
            if cur_char.isalpha():
                for new_char in [cur_char.upper(), cur_char.lower()]:
                    path.append(new_char)
                    self.dfs(S, path, res, i + 1)
                    path.pop()
            else:
                path.append(cur_char)
                self.dfs(S, path, res, i + 1)
                path.pop()