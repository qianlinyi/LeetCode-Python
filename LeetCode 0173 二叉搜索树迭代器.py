# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.num = deque()

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            self.num.append(node.val)
            inOrder(node.right)

        inOrder(root)

    def next(self) -> int:
        if len(self.num):
            return self.num.popleft()

    def hasNext(self) -> bool:
        return len(self.num) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
