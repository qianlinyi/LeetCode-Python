from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)

        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            height[node] = 1 + max(get_height(node.left), get_height(node.right))
            return height[node]

        get_height(root)

        res = [0 for i in range(len(height) + 1)]

        def dfs(node: Optional[TreeNode], depth: int, rest: int) -> None:
            if not node:
                return
            depth += 1
            res[node.val] = rest
            dfs(node.left, depth, max(rest, depth + height[node.right]))
            dfs(node.right, depth, max(rest, depth + height[node.left]))

        dfs(root, -1, 0)
        return [res[_] for _ in queries]
