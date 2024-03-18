class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sums=n*(n+1)//2
        for i in nums:
            sums-=i
        return sums

        