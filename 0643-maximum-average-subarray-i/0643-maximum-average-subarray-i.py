class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k==1:
            return max(nums)/k
        else:
            avgs = sum(nums[0:k])/k
            maxval = sum(nums[0:k])/k
            for i in range(len(nums)-k):
                avgs = avgs-nums[i]/k + nums[k+i]/k
                maxval = max(avgs,maxval)
            return maxval
        