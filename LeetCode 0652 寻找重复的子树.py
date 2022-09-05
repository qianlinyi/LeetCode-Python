# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 三元组字典 + DFS
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            triple = (node.val, dfs(node.left), dfs(node.right))
            if triple in d:
                (tree, id) = d[triple]
                ans.add(tree)
                return id
            else:
                nonlocal index
                index += 1
                d[triple] = (node, index)
                return index

        index = 0
        d = dict()
        ans = set()

        dfs(root)
        return list(ans)
