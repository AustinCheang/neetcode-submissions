# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n) | Space: O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lower_bound, upper_bound):
            if not node:
                return True

            if lower_bound >= node.val or upper_bound <= node.val:
                return False

            return validate(node.left, lower_bound, node.val) and validate(node.right, node.val, upper_bound)
        
        return validate(root, float('-inf'), float('inf'))