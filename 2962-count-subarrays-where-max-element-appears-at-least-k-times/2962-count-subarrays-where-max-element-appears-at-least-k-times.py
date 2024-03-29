class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxval = max(nums)
        counts=0
        scount=0
        j=0
        for i in nums:
            if i==maxval:
                scount+=1
            while scount == k:
                if nums[j]==maxval:
                    scount-=1
                j+=1
            counts+=j
        return counts