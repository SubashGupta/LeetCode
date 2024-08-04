class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        op = [0]*(n+1)
        for i in trust:
            a=i[0]
            b=i[1]
            op[a] -=1
            op[b] +=1
        for i in range(1,n+1):
            if op[i]==n-1:
                return i
        else:
            return -1 

                    