class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d={}
        index=0
        for i in bills:
            index+=1
            val1 = d.get(5,0)
            val2 = d.get(10,0)
            if i == 5:
                d[i] = d.get(i,0)+1
            elif i == 10:
                diff = 5
                d[i] = d.get(i,0)+1
                val1 = d.get(5,0)
                if val1:
                    d[diff]-=1
                else:
                    return False
            elif i == 20:
                diff = 15
                d[i] = d.get(i,0)+1
                if val1 or val2:
                    while diff != 0:
                        val1 = d.get(5,0)
                        val2 = d.get(10,0)
                        if diff > 5 and val2:
                            d[10]-=1
                            diff-=10
                        elif diff >= 5 and val1:
                            d[5]-=1
                            diff-=5
                        else:
                            return False
                else:
                    return False
        return True