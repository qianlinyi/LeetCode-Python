# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            next = root.right
            while next.left:
                next = next.left  # 二叉搜索树性质，右子树的最小节点替代根节点
            next.right = self.deleteNode(root.right, next.val)  # 删去右子树的最小节点
            next.left = root.left
            return next
        return root
