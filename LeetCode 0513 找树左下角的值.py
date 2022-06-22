# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = h = 0

        def dfs(node: Optional[TreeNode], height: int) -> int:
            if not node:
                return
            height += 1
            dfs(node.left, height)
            dfs(node.right, height)
            nonlocal ans, h
            if height > h:
                h = height
                ans = node.val

        dfs(root, 0)
        return ans
