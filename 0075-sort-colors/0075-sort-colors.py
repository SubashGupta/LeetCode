class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        j=0
        k=len(nums)-1
        n=len(nums)
        while i<=k:
            if nums[i]==0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i] == 1:
                i+=1
            elif nums[i]==2:
                nums[k],nums[i]=nums[i],nums[k]
                k-=1
        return nums
        