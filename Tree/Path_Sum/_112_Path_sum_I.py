class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum - root.val == 0
        l = self.hasPathSum(root.left, sum - root.val)
        r = self.hasPathSum(root.right, sum - root.val)
        return l or r