# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    # Time Complexity: O(n), inorder O(n) + buildBST O(n) =>  O(n)
    # Space Complexity: O(n), nodes O(n) + recursive call O(logN) =>  O(n) 
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.inorder(root, nodes)
        return self.buildBST(nodes, 0, len(nodes)-1)


    def inorder(self, root: TreeNode, nodes):
        if not root:
            return 
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)

    def buildBST(self, nodes, left, right) -> TreeNode:
        if left > right:
            return None
        mid = (left + right)//2
        node = nodes[mid]
        node.left = self.buildBST(nodes, left, mid-1)
        node.right = self.buildBST(nodes, mid+1, right)
        return node
            
# class Solution:
    
#     def makeVine(self, grand, count=0):
#         node = grand.right
#         while node:
#             if node.left:
#                 old_node = node
#                 node = node.left
#                 old_node.left = node.right
#                 node.right = old_node
#                 grand.right = node
#             else:
#                 count += 1
#                 grand = node
#                 node = node.right
#         return count
    
#     def compress(self, grand, m):
#         node = grand.right
#         while m > 1:
#             m-=1
#             old_node = node
#             node = node.right
#             grand.right = node
#             old_node.right = node.left
#             node.left = old_node
#             grand = node
#             node = node.right
    
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#         grand = TreeNode()
#         grand.right = root
#         count = self.makeVine(grand)
#         height = int(log2(count+1))
#         remaining_nodes = pow(2, height) - 1
#         self.compress(grand, count-remaining_nodes)
#         while remaining_nodes > 0:
#             remaining_nodes /= 2
#             self.compress(grand, remaining_nodes)
#         return grand.right