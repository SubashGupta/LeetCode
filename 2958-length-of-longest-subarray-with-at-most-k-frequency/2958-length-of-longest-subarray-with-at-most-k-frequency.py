class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        m=Counter()
        l=0
        i=0
        flag=0
        for j in range(len(nums)):
            m[nums[j]]+=1
            if m[nums[j]]==k+1:
                flag+=1
            if flag:
                m[nums[i]]-=1
                if m[nums[i]] == k:
                    flag -=1
                i+=1
        return len(nums)-i