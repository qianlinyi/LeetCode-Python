class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def dfs(s: str, num: int) -> None:
            if num == len(digits):
                ans.append(s)
                return
            for c in d[digits[num]]:
                dfs(s + c, num + 1)

        if digits == '':
            return ans
        dfs('', 0)
        return ans
