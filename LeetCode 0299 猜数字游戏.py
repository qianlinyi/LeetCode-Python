class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt1, cnt2 = Counter(secret), Counter(guess)
        A = B = 0
        for i, c in enumerate(guess):
            if c == secret[i]:
                A += 1
                cnt1[c] -= 1
                cnt2[c] -= 1
        for i, c in enumerate(guess):
            if c != secret[i] and cnt1[c] and cnt2[c]:
                cnt1[c] -= 1
                cnt2[c] -= 1
                B += 1
        return f'{cnt1}A{cnt2}B'
