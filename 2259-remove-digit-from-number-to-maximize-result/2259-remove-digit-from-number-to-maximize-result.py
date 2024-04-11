class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxi=float('-inf')
        for i in range(len(number)):
            x=number[:]
            if number[i] == digit:
                x = number[:i]+number[i+1:]
                maxi =max(maxi, int(x))
        return str(maxi)
        