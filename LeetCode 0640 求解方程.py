# 模拟
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        if left[0] not in ['+', '-']:
            left = '+' + left
        if right[0] not in ['+', '-']:
            right = '+' + right

        def splitEquation(equation: str) -> tuple:
            index, cnt, sum = 0, 0, 0
            while index < len(equation):
                sign = 1 if equation[index] == '+' else -1
                index += 1
                num, valid = 0, 0
                while index < len(equation) and equation[index].isdigit():
                    valid = 1
                    num = num * 10 + ord(equation[index]) - ord('0')
                    index += 1
                if index < len(equation) and equation[index] == 'x':
                    cnt += sign * (num if valid else 1)
                    index += 1
                else:
                    sum += sign * num
            return cnt, sum

        cntl, suml = splitEquation(left)
        cntr, sumr = splitEquation(right)
        if cntl == cntr and suml == sumr:
            return 'Infinite solutions'
        elif cntl == cntr and suml != sumr:
            return 'No solution'
        else:
            return f'x={(sumr - suml) // (cntl - cntr)}'
