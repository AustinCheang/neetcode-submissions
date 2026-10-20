# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n) | Space: O(log n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self._check_height_and_balance(root)
        return result != -1

    def _check_height_and_balance(self, node):
        if not node:
            return 0

        left_height = self._check_height_and_balance(node.left)
        if left_height == -1:
            return -1

        right_height = self._check_height_and_balance(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)