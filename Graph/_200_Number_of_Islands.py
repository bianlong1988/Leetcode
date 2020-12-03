import collections
"""
Input:
11000
11000
00100
00011

Output: 3

"""


grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

# Option 1: DFS (Time: m*n ; Space: m*n)
class Solution1(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numOfIsland = 0
        if not grid or len(grid) == 0:
            return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    numOfIsland += self.dfs(grid, r, c)
        return numOfIsland

    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
            return 0
        grid[r][c] = '0'

        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
        return 1
        
# iteration DFS
class Solution2():
    def numIslands(self, grid):
        if not grid or len(grid) == 0:
            return 0
        num_of_island = 0
        stack = []
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1': # do dfs on '1' (islands)
                    num_of_island += 1
                    stack.append((r,c))
                    while stack:
                        r, c = stack.pop()  #(r, c)
                        if grid[r][c] == '1': # if island, then visited
                            grid[r][c] = '0'
                            if r - 1 >= 0:
                                stack.append((r - 1, c))
                            if r + 1 < R:
                                stack.append((r + 1, c))
                            if c - 1 >= 0:
                                stack.append((r , c - 1))
                            if c + 1 < C:
                                stack.append((r, c + 1))
        return num_of_island
# iteration BFS
class Solution3():
    def numIslands(self, grid):
        if not grid or len(grid) == 0:
            return 0
        num_of_island = 0
        queue = collections.deque()
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1': # do dfs on '1' (islands)
                    num_of_island += 1
                    queue.append((r,c))
                    while queue:
                        r, c = queue.popleft()  #(r, c)
                        if grid[r][c] == '1': # if island, then visited
                            grid[r][c] = '0'
                            if r - 1 >= 0:
                                queue.append((r - 1, c))
                            if r + 1 < R:
                                queue.append((r + 1, c))
                            if c - 1 >= 0:
                                queue.append((r , c - 1))
                            if c + 1 < C:
                                queue.append((r, c + 1))
        return num_of_island

if __name__ == "__main__":
    s = Solution1()
    print "solution: ", s.numIslands(grid)