# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, val: int) -> int:
        queue = deque()
        queue.append(self.root)
        while queue:
            siz = len(queue)
            for _ in range(siz):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = TreeNode(val)
                    return node.val
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = TreeNode(val)
                    return node.val

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
