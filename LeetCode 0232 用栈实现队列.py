class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def move(self) -> None:
        while len(self.q1):
            self.q2.append(self.q1.pop())

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if len(self.q2) == 0:
            self.move()
        return self.q2.pop()

    def peek(self) -> int:
        if len(self.q2) == 0:
            self.move()
        return self.q2[-1]

    def empty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
