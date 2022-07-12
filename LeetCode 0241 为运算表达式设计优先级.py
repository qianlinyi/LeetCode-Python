from typing import List


# 分治
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        ans = []
        for i, c in enumerate(expression):
            if c in ['+', '-', '*']:
                # 分解，遇到运算符计算左右两侧的结果集
                leftpart = self.diffWaysToCompute(expression[:i])
                rightpart = self.diffWaysToCompute(expression[i + 1:])
                # 合并，根据运算符合并子问题的解
                for left in leftpart:
                    for right in rightpart:
                        if c == '+':
                            ans.append(left + right)
                        elif c == '-':
                            ans.append(left - right)
                        else:
                            ans.append(left * right)
        return ans
