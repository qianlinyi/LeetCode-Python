# 状态机
from collections import defaultdict
from enum import Enum, auto


class ExprStatus(Enum):
    VALUE = auto()  # 初始状态
    NONE = auto()  # 表达式类型未知
    LET = auto()  # let 表达式
    LET1 = auto()  # let 表达式已经解析了 vi 变量
    LET2 = auto()  # let 表达式已经解析了最后一个表达式 expr
    ADD = auto()  # add 表达式
    ADD1 = auto()  # add 表达式已经解析了 e1 表达式
    ADD2 = auto()  # add 表达式已经解析了 e2 表达式
    MULT = auto()  # mult 表达式
    MULT1 = auto()  # mult 表达式已经解析了 e1 表达式
    MULT2 = auto()  # mult 表达式已经解析了 e2 表达式
    DONE = auto()  # 解析完成


class Expr:
    __slots__ = 'status', 'var', 'value', 'e1', 'e2'

    def __init__(self, status):
        self.status = status
        self.var = ''  # let 的变量 vi
        self.value = 0  # VALUE 状态的数值，或者 LET2 状态最后一个表达式的数值
        self.e1 = self.e2 = 0  # add 或 mult 表达式的两个表达式 e1 和 e2 的数值


class Solution:
    def evaluate(self, expression: str) -> int:
        scope = defaultdict(list)

        def calculateToken(token: str) -> int:
            return scope[token][-1] if token[0].islower() else int(token)

        vars = []
        s = []
        cur = Expr(ExprStatus.VALUE)
        i, n = 0, len(expression)
        while i < n:
            if expression[i] == ' ':
                i += 1  # 去掉空格
                continue
            if expression[i] == '(':
                i += 1  # 去掉左括号
                s.append(cur)
                cur = Expr(ExprStatus.NONE)
                continue
            if expression[i] == ')':  # 本质上是把表达式转成一个 token
                i += 1  # 去掉右括号
                if cur.status is ExprStatus.LET2:
                    token = str(cur.value)
                    for var in vars[-1]:
                        scope[var].pop()  # 清除作用域
                    vars.pop()
                elif cur.status is ExprStatus.ADD2:
                    token = str(cur.e1 + cur.e2)
                else:
                    token = str(cur.e1 * cur.e2)
                cur = s.pop()  # 获取上层状态
            else:
                i0 = i
                while i < n and expression[i] != ' ' and expression[i] != ')':
                    i += 1
                token = expression[i0:i]

            if cur.status is ExprStatus.VALUE:
                cur.value = int(token)
                cur.status = ExprStatus.DONE
            elif cur.status is ExprStatus.NONE:
                if token == "let":
                    cur.status = ExprStatus.LET
                    vars.append([])  # 记录该层作用域的所有变量, 方便后续的清除
                elif token == "add":
                    cur.status = ExprStatus.ADD
                elif token == "mult":
                    cur.status = ExprStatus.MULT
            elif cur.status is ExprStatus.LET:
                if expression[i] == ')':  # let 表达式的最后一个 expr 表达式
                    cur.value = calculateToken(token)
                    cur.status = ExprStatus.LET2
                else:
                    cur.var = token
                    vars[-1].append(token)  # 记录该层作用域的所有变量, 方便后续的清除
                    cur.status = ExprStatus.LET1
            elif cur.status is ExprStatus.LET1:
                scope[cur.var].append(calculateToken(token))
                cur.status = ExprStatus.LET
            elif cur.status is ExprStatus.ADD:
                cur.e1 = calculateToken(token)
                cur.status = ExprStatus.ADD1
            elif cur.status is ExprStatus.ADD1:
                cur.e2 = calculateToken(token)
                cur.status = ExprStatus.ADD2
            elif cur.status is ExprStatus.MULT:
                cur.e1 = calculateToken(token)
                cur.status = ExprStatus.MULT1
            elif cur.status is ExprStatus.MULT1:
                cur.e2 = calculateToken(token)
                cur.status = ExprStatus.MULT2
        return cur.value
