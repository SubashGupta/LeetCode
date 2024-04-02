class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s)-1
        count=0
        strlen=0
        while last>=0 and s[last] == ' ':
            count+=1
            last-=1
        while last>=0 and s[last] != ' ':
            strlen+=1
            last-=1
        return strlen
        