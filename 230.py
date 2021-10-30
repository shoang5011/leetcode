"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def inorder(node):
#             if not node: 
#                 return []
#             return inorder(node.left) + [node.val] + inorder(node.right)
        
#         return inorder(root)[k-1]
            
        stack = []
        
        while True:         
            while root: 
                stack.append(root)
                root = root.left
            root = stack.pop()
            #check for k 
            k-=1
            if not k: 
                return root.val
            root = root.right
        