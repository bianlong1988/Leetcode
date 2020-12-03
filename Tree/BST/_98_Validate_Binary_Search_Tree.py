"""
    10 (-inf, +inf)
   / \
  0  30 (10, +inf)
     / \
   20   40
(10, 30) (30,inf)
"""



class Solution(object):
    def isValidBST(self, root):
        return self.isValid(root, None, None)

    def isValid(self, root, minVal, maxVal):
        if not root:
            return True
        if minVal and root.val <= minVal.val:
            return False
        if maxVal and root.val >= maxVal.val:
            return False

        l = self.isValid(root.left, minVal, root)
        r = self.isValid(root.right, root, maxVal)
        return l and r

