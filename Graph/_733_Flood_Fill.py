"""
Option 1: DFS
    Time O(n), Space O(n)
Option 2: BFS
"""
"""
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

[1,1,1]
[1,1,0]
[1,0,1]
"""
# Difference compare to other problem: do not need additional list to keep tracking the connection.
# -> no for loop needed, no disconnection in the matrix, will visit all the (r, c).


# Option 3: Recursive
class Solution3(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        self.dfs(sr, sc, image, oldColor, newColor)
        return image

    def dfs(self, r, c, image, oldColor, newColor):
        R, C = len(image), len(image[0])
        # base case
        if r < 0 or r >= R or c < 0 or c >= C or image[r][c] != oldColor:
            return
        image[r][c] = newColor
        # recursive calls
        self.dfs(r - 1, c, image, oldColor, newColor)
        self.dfs(r + 1, c, image, oldColor, newColor)
        self.dfs(r, c - 1, image, oldColor, newColor)
        self.dfs(r, c + 1, image, oldColor, newColor)



# Option 1: iteration DFS
class Solution1(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        len_c, len_r = len(image[0]), len(image)
        stack = [(sr, sc)]
        oldColor = image[sr][sc]

        if image[sr][sc] == newColor:
            return image

        while stack:
            r, c = stack.pop()
            if image[r][c] == oldColor:
                image[r][c] = newColor
                if r + 1 < len_r:
                    stack.append((r + 1, c))
                if r - 1 >= 0:
                    stack.append((r - 1, c))
                if c + 1 < len_c:
                    stack.append((r, c + 1))
                if c - 1 >= 0:
                    stack.append((r, c - 1))
        return image

# Option 2: Iteration BFS
import collections
class Solution2(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        len_c, len_r = len(image[0]), len(image)
        queue = collections.deque()
        queue.append((sr, sc))
        oldColor = image[sr][sc]

        if image[sr][sc] == newColor:
            return image

        while queue:
            r, c = queue.popleft()
            if image[r][c] == oldColor:
                image[r][c] = newColor
                if r + 1 < len_r:
                    queue.append((r + 1, c))
                if r - 1 >= 0:
                    queue.append((r - 1, c))
                if c + 1 < len_c:
                    queue.append((r, c + 1))
                if c - 1 >= 0:
                    queue.append((r, c - 1))
        return image

solution = Solution3()
print solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2)
