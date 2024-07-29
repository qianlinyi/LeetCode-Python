from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q, ans = [], []
        q.append(root)
        while q:
            res, temp, q = [], q, []
            for node in temp:
                res.append(node.val)
                if node.children is None:
                    continue
                for child in node.children:
                    q.append(child)
            ans.append(res)
        return ans


if __name__ == '__main__':
    root = Node(val=1)
    node1 = Node(val=3)
    node2 = Node(val=2)
    node3 = Node(val=4)
    root.children = [node1, node2, node3]
    node4 = Node(val=5)
    node5 = Node(val=6)
    node1.children = [node4, node5]
    s = Solution()
    print(s.levelOrder(root))
