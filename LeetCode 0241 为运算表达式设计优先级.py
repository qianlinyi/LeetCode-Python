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
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                # 合并，根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if c == '+':
                            ans.append(l + r)
                        elif c == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
        return ans
