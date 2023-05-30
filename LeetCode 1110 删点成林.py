# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        q = deque([root])
        to_delete = Counter(to_delete)
        ans = []
        if root.val not in to_delete:
            ans.append(root)
        while q:
            a = q.popleft()
            if a.val in to_delete:
                if a.left and a.left.val not in to_delete:
                    ans.append(a.left)
                if a.right and a.right.val not in to_delete:
                    ans.append(a.right)
            if a.left:
                q.append(a.left)
                if a.left.val in to_delete:
                    a.left = None
            if a.right:
                q.append(a.right)
                if a.right.val in to_delete:
                    a.right = None
        return ans
