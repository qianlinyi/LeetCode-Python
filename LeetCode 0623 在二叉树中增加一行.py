# Definition for a binary tree node.
from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newroot = TreeNode(val)
            newroot.left = root
            return newroot
        q, d = [root], 1
        while q:
            temp = []
            for node in q:
                tmpl = node.left
                tmpr = node.right
                if tmpl:
                    temp.append(tmpl)
                if tmpr:
                    temp.append(tmpr)
                if d == depth - 1:
                    newnodel = TreeNode(val)
                    newnoder = TreeNode(val)
                    node.left = newnodel
                    newnodel.left = tmpl
                    node.right = newnoder
                    newnoder.right = tmpr
            q = temp
            d += 1
        return root
