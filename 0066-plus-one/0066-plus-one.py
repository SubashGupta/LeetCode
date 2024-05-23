class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total=0
        size=len(digits)
        for i in digits:
            total=total*10+i
        total+=1
        if len(str(total)) > size:
            digits.append(total%10)
            total=total//10
        for i in range(size-1,-1,-1):
            digits[i] = total%10
            total=total//10
        return digits
        