class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for i in bills:
            if i == 5:
                five+=1
            elif i == 10:
                ten+=1
                diff = 5
                if five:
                    five-=1
                else:
                    return False
            else:
                diff = 15
                if five and ten:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True