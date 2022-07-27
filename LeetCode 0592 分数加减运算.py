import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0].isdigit():
            expression = '+' + expression
        expression = expression[::-1]
        numerator, denominator, index = [], [], 0
        while index < len(expression):
            if expression[index].isdigit():
                num = ''
                while expression[index].isdigit():
                    num = expression[index] + num
                    index += 1
                if expression[index] == '/':
                    denominator.append(int(num))
                elif expression[index] == '+':
                    numerator.append(int(num))
                elif expression[index] == '-':
                    numerator.append(-int(num))
            else:
                index += 1
        ans1, ans2 = 0, math.lcm(*denominator)
        if ans2 == 0:
            ans1 = 1
        else:
            for i in range(len(numerator)):
                ans1 += ans2 // denominator[i] * numerator[i]
            gcd = math.gcd(ans1, ans2)
            ans1, ans2 = ans1 // gcd, ans2 // gcd
        return str(ans1) + '/' + str(ans2)
