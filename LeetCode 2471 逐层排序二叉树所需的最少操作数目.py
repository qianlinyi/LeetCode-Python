# Definition for a binary tree node.
from bisect import bisect_left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def fuck(a: List[int]) -> int:
            b = sorted(a)
            n, a = len(b), [bisect_left(b, _) for _ in a]
            loops = 0
            vis = [False for _ in range(n)]
            for v in a:
                if vis[v]:
                    continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                loops += 1
            return n - loops

        q = [root]
        ans = 0
        while q:
            temp = q
            q = []
            val = []
            for node in temp:
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += fuck(val)
        return ans
