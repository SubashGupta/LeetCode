class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        j=0
        d={}
        sums = nums[0]
        for i in range(1,len(nums)):
            sums+=nums[i]
            x=d.get(sums,'e')
            if x != 'e':
                return True
            else:
                d[sums] = (i-1,i)
                sums-=nums[j]
                j+=1
        return False
        