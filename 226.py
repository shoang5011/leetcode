"""
Given the root of a binary tree, invert the tree, and return its root.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if not root: 
            return None
        
#         left = self.invertTree(root.left)
#         right= self.invertTree(root.right)
#         root.left = right
#         root.right = left 
#         return root 
        
        
        def recursive(node):
            if not node: 
                return
            
            tmp = node.left 
            node.left = node.right
            node.right = tmp
            recursive(node.left)
            recursive(node.right)
            
        recursive(root)
        return root
            
        