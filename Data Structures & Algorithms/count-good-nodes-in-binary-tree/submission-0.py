# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n) | Space: O(n)
    def goodNodes(self, root: Optional[TreeNode], path_max = float('-inf')) -> int:
        if not root:
            return 0

        left = self.goodNodes(root.left, max(path_max, root.val))
        right = self.goodNodes(root.right, max(path_max, root.val))

        return left + right + int(path_max <= root.val)