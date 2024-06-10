class MyQueue:

    def __init__(self):
        self.nums=[]
        self.dummy=[]
    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> int:
        while len(self.nums)!=1:
            temp=self.nums.pop()
            self.dummy.append(temp)
        final=self.nums.pop()
        while len(self.dummy)!=0:
            temp=self.dummy.pop()
            self.nums.append(temp)
        return final
    
    def peek(self) -> int:
        return self.nums[0]

    def empty(self) -> bool:
        if len(self.nums)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()