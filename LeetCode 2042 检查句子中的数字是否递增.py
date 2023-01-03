class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = [int(token) for token in s.split(' ') if all(c.isdigit() for c in token)]
        return all(num[i - 1] < num[i] for i in range(1, len(num)))
