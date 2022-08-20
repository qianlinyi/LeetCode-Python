# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        val, pos = max(nums), nums.index(max(nums))
        root = TreeNode(val, left=self.constructMaximumBinaryTree(nums[:pos]),
                        right=self.constructMaximumBinaryTree(nums[pos + 1:]))
        return root
