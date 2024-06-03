class Solution:
    def isPalindrome(self, s: str) -> bool:
        op=''
        for i in s:
            if (ord(i)>=97 and ord(i)<=122)  or (ord(i)>=65 and ord(i)<=90):
                op+=i.lower()
            elif ord(i)>=48 and ord(i)<=57:
                op+=i
        if op[::-1] == op:
            return True
        else:
            return False