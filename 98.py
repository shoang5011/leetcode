# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        #### Using stack to add all root node, inorder traverse
        # stack = []
        # left_child_val = float(-inf)
        # while stack or root: 
        #     while root: 
        #         stack.append(root)
        #         root = root.left
            
        #     root = stack.pop()
        #     if root.val <= left_child_val: 
        #         return False 
        #     left_child_val = root.val
        #     root = root.right
        # return True



        ##### recursive, using left and right bound. For left child, -inf for left and root val for right . Reverse for right child
        def helper(node,left,right): 
            if not node: 
                return True 

            if not (node.val < right and node.val > left): 
                return False

            return helper(node.left, left,node.val) & helper(node.right,node.val,right)

        return helper(root,float('-inf'),float("inf"))


