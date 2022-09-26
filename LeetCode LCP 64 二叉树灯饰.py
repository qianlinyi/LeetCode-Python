# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 树形DP
# 记录四种状态：当前节点及子节点全关/开，当前节点开、子节点关，当前节点关、子节点开
class Solution:
    def closeLampInTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> List[int]:
            if node is None:
                return [0, 0, 0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == 0:
                # 当前节点及子节点全关
                allClose = min(left[0] + right[0], left[1] + right[1] + 2, left[2] + right[2] + 2,
                               left[3] + right[3] + 2)

                # 当前节点及子节点全开
                allOpen = min(left[0] + right[0] + 1, left[1] + right[1] + 1, left[2] + right[2] + 3,
                              left[3] + right[3] + 1)

                # 当前节点开、子节点关
                subAllClose = min(left[0] + right[0] + 1, left[1] + right[1] + 1, left[2] + right[2] + 1,
                                  left[3] + right[3] + 3)

                # 当前节点关、子节点开
                subAllOpen = min(left[0] + right[0] + 2, left[1] + right[1], left[2] + right[2] + 2,
                                 left[3] + right[3] + 2)
            else:
                allClose = min(left[0] + right[0] + 1, left[1] + right[1] + 1, left[2] + right[2] + 1,
                               left[3] + right[3] + 3)
                allOpen = min(left[0] + right[0] + 2, left[1] + right[1], left[2] + right[2] + 2,
                              left[3] + right[3] + 2)
                subAllClose = min(left[0] + right[0], left[1] + right[1] + 2, left[2] + right[2] + 2,
                                  left[3] + right[3] + 2)
                subAllOpen = min(left[0] + right[0] + 1, left[1] + right[1] + 1, left[2] + right[2] + 3,
                                 left[3] + right[3] + 1)
            return [allClose, allOpen, subAllClose, subAllOpen]

        return dfs(root)[0]
