# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def checkSufficientLeaf(node, sum, limit):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return node.val + sum >= limit
            haveSufficientLeft = checkSufficientLeaf(node.left, sum + node.val, limit)
            haveSufficientRight = checkSufficientLeaf(node.right, sum + node.val, limit)
            if not haveSufficientLeft:
                node.left = None
            if not haveSufficientRight:
                node.right = None
            return haveSufficientLeft or haveSufficientRight

        havaSufficent = checkSufficientLeaf(root, 0, limit)
        return root if havaSufficent else None
