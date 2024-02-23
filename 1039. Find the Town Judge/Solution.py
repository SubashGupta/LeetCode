class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        lst=[0]*(n+1)
        for i in trust:
            a=i[0]
            b=i[1]
            lst[a] -=1
            lst[b] +=1
        for i in range(1, len(lst)):
            if lst[i]==n-1:
                return i
        return -1


                    