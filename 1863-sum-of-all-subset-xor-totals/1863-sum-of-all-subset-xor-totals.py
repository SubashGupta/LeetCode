class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            total|=i
        return total<<(len(nums)-1)
        