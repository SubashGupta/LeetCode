class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        d={0:-1}
        for i in  range(len(nums)):
            prefix=(prefix+nums[i])%k
            if prefix in d:
                if i-d[prefix] > 1:
                    return True
            else:
                d[prefix] = i
        return False