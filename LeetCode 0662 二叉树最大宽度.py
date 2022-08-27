# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, ans = [[root, 1]], 0
        while q:
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            temp = q
            q = []
            for node, index in temp:
                if node.left:
                    q.append([node.left, index * 2])
                if node.right:
                    q.append([node.right, index * 2 + 1])
        return ans
