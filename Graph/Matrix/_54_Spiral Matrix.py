"""
time: O(m*n)
space: O(m*n)
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        # minus 1 to avoid index issue at boundry
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        size = len(matrix) * len(matrix[0])

        res = []
        while len(res) < size:
            # range need to be added 1
            for col in range(left, right + 1):
                if len(res) < size:
                    res.append(matrix[top][col])
            top += 1
            # range need to be added 1
            for row in range(top, bottom + 1):
                if len(res) < size:
                    res.append(matrix[row][right])
            right -= 1
            for col in range(right, left - 1, -1):
                if len(res) < size:
                    res.append(matrix[bottom][col])
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                if len(res) < size:
                    res.append(matrix[row][left])
            left += 1
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print s.spiralOrder(matrix)