class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        
        while tickets[k] !=0:
            i=0
            while i<len(tickets):   
                if tickets[i]!=0:
                    tickets[i]-=1
                    time+=1
                else:
                    pass
                if tickets[k] == 0:
                    break
                i+=1
        return time