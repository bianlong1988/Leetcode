input = [1,2,3]


class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        rst = [[]]
        for i in nums:
            nxt_rst = []
            for j in rst:
                #find a index to insert a new letter, leftmost: 0, rightmost: len(i)
                for k in range(len(j) + 1):
                    nxt_rst.append(j[:k] + [i] + j[k:])
            rst = nxt_rst
        return rst


class Solution3():
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]

    """

    def permute(self, nums):
        visited = [False] * len(nums)
        res = []
        self.backtracking(res, visited, [], nums)
        return res

    def backtracking(self, res, visited, path, nums):
        if len(path) == len(nums):
            res.append(path)
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                path.append(nums[i])
                self.backtracking(res, visited, path[:], nums)
                visited[i] = False
                path.pop()



if __name__ == '__main__':
    s = Solution3()
    print s.permute(input)
