class Solution:
    def isPalindrome(self, x: int) -> bool:
        ip = str(x)
        if ip == ip[::-1]:
            return True
        else:
            return False
        