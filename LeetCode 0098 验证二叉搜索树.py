# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def judge(node: Optional[TreeNode], lower=float('-inf'), upper=float('inf')) -> bool:
            if node is None:
                return True
            val = node.val
            return lower < val < upper and judge(node.left, lower, val) and judge(node.right, val, upper)

        return judge(root)
