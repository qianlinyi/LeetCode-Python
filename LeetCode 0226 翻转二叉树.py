# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = TreeNode()
        if not root:
            return None
        if root:
            ans.val = root.val
        if root.right:
            ans.left = self.invertTree(root.right)
        if root.left:
            ans.right = self.invertTree(root.left)
        return ans