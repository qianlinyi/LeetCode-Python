class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = dict()
        for k, v in knowledge:
            mp[k] = v
        flag = False
        word = ''
        ans = ''
        for c in s:
            if c == ')':
                flag = False
                if word in mp:
                    ans += mp[word]
                else:
                    ans += '?'
                word = ''
            if flag:
                word += c
            else:
                ans += c
            if c == '(':
                flag = True
        return ans
