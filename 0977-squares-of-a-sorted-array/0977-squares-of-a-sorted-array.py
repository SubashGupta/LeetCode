class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        gap=ceil(len(nums)/2)
        counts=0
        while gap>0:
            i=0
            j=gap
            while j<len(nums):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            if gap == 1:
                break
            gap=ceil(gap/2)
        return nums
                    
                    
            
            
        