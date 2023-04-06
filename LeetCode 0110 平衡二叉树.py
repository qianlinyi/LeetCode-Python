# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHead = height(root.right)
            if leftHeight == -1 or rightHead == -1 or abs(leftHeight - rightHead) > 1:
                return -1
            else:
                return max(leftHeight, rightHead) + 1

        return height(root) >= 0
