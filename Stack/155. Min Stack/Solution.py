class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []
        

    def push(self, val: int) -> None:
        currentMin = min(val, self.minSt[-1]) if self.minSt else val
        self.st.append(val)
        self.minSt.append(currentMin)
        

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
