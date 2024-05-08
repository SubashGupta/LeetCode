class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxi = max(score)
        lst = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        c=0
        for i in range(maxi,-1, -1):
            if i in score:
                if c<=2:
                    index1 = score.index(i)
                    score[index1] = lst[c]
                    c+=1
                else:
                    index1 = score.index(i)
                    score[index1] = str(c+1)
                    c+=1
        return score
            
        