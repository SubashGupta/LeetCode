class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        maxi=0
        c=1
        if len(set(nums))<2:
            return len(set(nums))
        for i in set(nums):
            d[i] = 1
        for i in nums:
            case1=i-1
            case2=i+1
            if not d.get(case1):
                if d.get(case2):
                    c=1
                    while d.get(case2):
                        case2+=1
                        c+=1
            maxi=max(c,maxi)
        return maxi