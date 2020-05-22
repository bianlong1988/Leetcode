class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if root.val == key:
            if root.right is None and root.left is None:
                return None
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                root.val = self.smallest(root.right)
                root.right = self.deleteNode(root.right, root.val)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
            
        return root
    
    def smallest(self,node):
        while node.left is not None:
            node = node.left
        return node.val