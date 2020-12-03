# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        elif root.val < val:
            root.right = self.insertIntoBST(root.right)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left)
        return root