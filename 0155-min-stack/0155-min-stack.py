class MinStack:

    def __init__(self):
        self.nums=[]
        self.minnums=[]

    def push(self, val: int) -> None:
        self.nums.append(val)
        if len(self.minnums)>0:
            if self.minnums[-1]> val:
                self.minnums.append(val)
            else:
                self.minnums.append(self.minnums[-1])
        else:
            self.minnums.append(val)

    def pop(self) -> None:
        if len(self.nums)>0:
            self.minnums.pop()
            return self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.minnums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()