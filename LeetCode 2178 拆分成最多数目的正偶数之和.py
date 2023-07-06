class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans = []
        if finalSum % 2:
            return ans
        base = 2
        while base <= finalSum:
            ans.append(base)
            finalSum -= base
            base += 2
        ans[-1] += finalSum
        return ans
