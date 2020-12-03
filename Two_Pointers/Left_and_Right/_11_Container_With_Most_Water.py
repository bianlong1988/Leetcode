
class Solution():
    """
    input type: List[int]
    rtype: int
    """
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_h = min(height[l], height[r])
            cur_area = (r - l) * max_h
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(cur_area, max_area)
        return max_area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    print s.maxArea(height)
