class Solution:
    def reverseWords(self, s: str) -> str:
        op1=''
        s = s.strip()
        lst=s.split(" ")
        print(lst)
        op=[]
        for i in lst:
            if len(i):
                op.append(i.strip())
        while len(op) != 1:
            op1+=op.pop()+' '
        op1+=op.pop()
        return op1