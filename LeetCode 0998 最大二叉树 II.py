# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        nums = []

        def inOrder(root: Optional[TreeNode]) -> None:
            if not root:
                return
            inOrder(root.left)
            nums.append(root.val)
            inOrder(root.right)

        inOrder(root)
        nums.append(val)

        def construct(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 0:
                return
            mx = max(nums)
            root = TreeNode(mx)
            root.left = construct(nums[0:nums.index(mx)])
            root.right = construct(nums[nums.index(mx) + 1:])
            return root

        return construct(nums)
