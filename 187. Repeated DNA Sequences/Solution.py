class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lst=[]
        for i in range(len(s)-10):
            x=s[i:i+10]
            if x in s[i+1:]:
                lst.append(x)
        return list(set(lst))   