
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.transform(root)
        return root
    
    def transform(self, node):
        if node is None:
            return
        
        # Traverse the right subtree first (reverse inorder traversal)
        self.transform(node.right)
        
        # Update the current node's value with the sum of greater values
        self.sum += node.val
        node.val = self.sum
        
        # Traverse the left subtree
        self.transform(node.left)
