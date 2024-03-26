class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        op=[]
        for i in nums:
            abso = abs(i)
            if nums[abso-1]<0:
                op.append(abso)
            else:
                nums[abso-1] *= -1
        return op
            
        