input = [1,1,2]

class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [False] * len(nums)
        nums.sort()
        res = []
        self.backtrack(nums, [], res, visited)
        return res

    def backtrack(self, nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path)
        for i in range(len(nums)):
            # skip if
            if visited[i]:
                print 'Skip 1.', ' Current index:', i
                continue
            # skip the current path if:
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1]:
                print 'Skip 2.', ' Current index:', i
                continue

            visited[i] = True
            path.append(nums[i])
            print 'current path: ', path, "| Visited: ", visited, '| index: ', i
            self.backtrack(nums, path[:], res, visited)
            visited[i] = False
            path.pop()
            print 'backtracking path: ', path, "| Visited: ", visited, '| index: ', i
if __name__ == '__main__':
    s = Solution1()
    print s.permuteUnique(input)
