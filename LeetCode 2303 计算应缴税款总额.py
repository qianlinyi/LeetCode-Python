class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans, pre = 0, 0
        for bracket in brackets:
            if income > bracket[0]:
                ans += (bracket[0] - pre) * bracket[1]
                pre = bracket[0]
            else:
                ans += (income - pre) * bracket[1]
                break
        return ans / 100
