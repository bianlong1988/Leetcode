class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        n = self.dfs(root, sum)     # perform dfs on all the node in the tree
        l = self.pathSum(root.left, sum) # traverse left
        r = self.pathSum(root.right, sum) # traverse right
        return n + l + r

    def dfs(self, root, sum):
        if not root:
            return 0

        n = int(root.val == sum) # if current node is a valid path, count 1, else 0
        l = self.dfs(root.left, sum - root.val)
        r = self.dfs(root.right, sum - root.val)
        return l + r + n