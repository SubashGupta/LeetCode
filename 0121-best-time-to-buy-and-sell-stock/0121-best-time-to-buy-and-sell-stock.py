class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minimal = float('inf')
        for i in prices:
            if i<minimal:
                minimal=i
            if i-minimal > profit:
                profit=i-minimal
        return profit
                
                    
        