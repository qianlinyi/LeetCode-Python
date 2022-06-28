from cmath import inf
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans, q = [], [root]
        if not root:
            return ans
        while q:
            mx, tmp, q = -inf, q, []
            for node in tmp:
                mx = max(mx, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(mx)
        return ans
