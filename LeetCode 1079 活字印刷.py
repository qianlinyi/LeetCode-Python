class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        cnt = Counter(tiles)

        def dfs(s, cnt):
            if len(s) > len(tiles):
                return
            if len(s):
                ans.add(s)
            for x in tiles:
                if cnt[x]:
                    cnt[x] -= 1
                    dfs(s + x, cnt)
                    cnt[x] += 1

        dfs('', cnt)
        return len(ans)
