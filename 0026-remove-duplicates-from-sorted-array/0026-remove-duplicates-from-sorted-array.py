class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1=0
        p2=1
        prev = nums[p1]
        while p2<len(nums):
            if prev == nums[p2]:
                p2+=1
            else:
                nums[p1+1], nums[p2] = nums[p2], nums[p1+1]
                p1+=1
                p2+=1
                prev = nums[p1]
        print(nums)
        return p1+1
        
                
        