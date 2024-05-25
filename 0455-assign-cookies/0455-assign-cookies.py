class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content=0
        index=0
        while index<len(s) and content<len(g):
            if s[index]>=g[content]:
                content+=1
            index+=1
        return content
        
            