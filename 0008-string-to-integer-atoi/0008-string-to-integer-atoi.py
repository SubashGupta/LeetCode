class Solution:
    def myAtoi(self, s: str) -> int:
        op=0
        negative=False
        flag=False
        sign = False
        dig=False
        for i in range(len(s)):
            if s[i] == " ":
                if op != 0 or sign:
                    break
                if dig:
                    return 0
                continue
            elif s[i] == "-":
                if (sign == True) or (s[i-1]!= " " and i!=0 and s[i-1].isdigit()):
                    break
                negative=True
                sign = True
            elif s[i] == "+":
                if (sign == True) or (s[i-1]!= " " and i!=0 and s[i-1].isdigit()):
                    break
                sign = True
            elif s[i]!= " " and s[i].isdigit() == False:
                break
            else:
                try:
                    x = int(s[i])
                    op=op*10+x
                    dig = True
                except:
                    flag = True
                    break
        if flag & op:
            if negative:
                op= -op
            if op>=2**31:    
                return 2**31 -1
            elif op<-2**31:
                return -2**31                
            else:
                return 0
        else:
            if negative:
                op= -op
            if op>=2**31:    
                return 2**31 -1
            elif op<-2**31:
                return -2**31                
            else:
                return op