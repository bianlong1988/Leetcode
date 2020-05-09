"""
Input:
11000
11000
00100
00011

Output: 3

"""

# Option 1: DFS (Time: m*n ; Space: m*n)
class Solution(object):
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
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
        else:
            grid[r][c] = '0'

        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
        return 1