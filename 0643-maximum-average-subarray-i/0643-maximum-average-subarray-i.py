class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k==1:
            return max(nums)/k
        if k==len(nums):
            return sum(nums)/k
        else:
            j=0
            n=len(nums)
            i=0
            maxs=float(-inf)
            sums=0
            while j<n:
                if j<k+i:
                    sums+=nums[j]
                    j+=1
                if j==k+i:
                    maxs=max(sums,maxs)
                    sums-=nums[i]
                    print(maxs,sums)
                    i+=1
                    sums+=nums[j]
                    j+=1
        maxs=max(sums,maxs)
        return maxs/k