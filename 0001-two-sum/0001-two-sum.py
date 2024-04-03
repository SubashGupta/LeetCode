class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums=0
        d={}
        for i in range(len(nums)):
            sums = target - nums[i]
            if sums in d:
                return i,d.get(sums)
            else:
                d[nums[i]] = i
                
                