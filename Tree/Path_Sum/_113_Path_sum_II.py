class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        self.dfs(root, sum, [], res)
        return res
# In Python, everything is a reference. So you build up your solutions as a list of many references to the same path, which eventually gets reduced to nothing.
    def dfs(self, root, sum, path, res):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            if root.val == sum:
                res.append(path)
        self.dfs(root.left, sum - root.val, path[:], res)
        self.dfs(root.right, sum - root.val, path[:], res)