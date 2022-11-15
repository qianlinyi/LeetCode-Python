from collections import defaultdict
from typing import List


# 字典树
class TrieTree:
    def __init__(self):
        self.son = defaultdict(TrieTree)
        self.idx = []
        self.score = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tree = TrieTree()
        for i, word in enumerate(words):
            cur = tree
            for c in word:
                cur = cur.son[c]
                cur.score += 1
            cur.idx.append(i)

        ans = [0 for _ in range(len(words))]

        def dfs(node: TrieTree, sum: int) -> None:
            sum += node.score
            for i in node.idx:
                ans[i] = sum
            for child in node.son.values():
                if child:
                    dfs(child, sum)

        dfs(tree, 0)
        return ans
