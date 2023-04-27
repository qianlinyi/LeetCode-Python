# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        cnt = Counter()  # 存当前节点所有儿子节点的值的和
        father = dict()  # 存每个节点的父亲节点
        father[root] = 0  # 根节点的父亲节点
        cnt[0] = root.val
        while q:
            tmp = q
            q = []
            s = sum(node.val for node in tmp)  # 求当前层所有节点的值的和
            for node in tmp:
                if node.left:
                    cnt[node] += node.left.val
                    father[node.left] = node
                    q.append(node.left)
                if node.right:
                    cnt[node] += node.right.val
                    father[node.right] = node
                    q.append(node.right)
                node.val = s - cnt[father[node]]
        return root
