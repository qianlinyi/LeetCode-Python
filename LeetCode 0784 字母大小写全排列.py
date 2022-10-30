class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def dfs(word: str, index: 0) -> None:
            if len(word) == len(s):
                ans.append(word)
            else:
                if s[index].isalpha():
                    dfs(word + s[index].lower(), index + 1)
                    dfs(word + s[index].upper(), index + 1)
                else:
                    dfs(word + s[index], index + 1)

        dfs('', 0)
        return ans
