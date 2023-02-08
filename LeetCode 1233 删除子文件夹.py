class Trie:
    def __init__(self):
        self.children = {}
        self.ref = -1


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for i, path in enumerate(folder):
            path = path.split('/')
            cur = trie
            for name in path:
                if name not in cur.children:
                    cur.children[name] = Trie()
                cur = cur.children[name]
            cur.ref = i

        ans = []

        def dfs(cur: Trie) -> None:
            if cur.ref != -1:
                ans.append(folder[cur.ref])
                return
            for child in cur.children.values():
                dfs(child)

        dfs(trie)
        return ans
