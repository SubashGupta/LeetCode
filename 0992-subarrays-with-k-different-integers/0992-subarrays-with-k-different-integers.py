class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subwindow(nums,k) -self.subwindow(nums,k-1)
    
    def subwindow(self, nums: List[int], k: int) -> int:
        d=Counter()
        final=0
        j=0
        for i in range(len(nums)):
            d[nums[i]]+=1
            while len(d) > k:
                d[nums[j]]-=1
                if d[nums[j]] == 0:
                    del d[nums[j]]
                j+=1
            final+=i-j+1
        return final
                
                
        