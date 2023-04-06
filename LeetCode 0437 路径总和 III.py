# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, cur):
            if not root:
                return 0
            res = 0
            cur += root.val
            res += prefix[cur - targetSum]
            prefix[cur] += 1
            res += dfs(root.left, cur)
            res += dfs(root.right, cur)
            prefix[cur] -= 1
            return res

        return dfs(root, 0)
