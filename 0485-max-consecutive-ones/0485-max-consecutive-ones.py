class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = float('-inf')
        c=0
        for index, i in enumerate(nums):
            if i == 1:
                c += 1
            else:
                maxcount = max(maxcount, c)
                c=0
        maxcount = max(maxcount, c)
        return maxcount
        