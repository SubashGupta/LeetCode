class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lst=set()
        for i in range(len(s)-10):
            x=s[i:i+10]
            if x in s[i+1:] and x not in lst:
                lst.add(x)
        return list(lst)  