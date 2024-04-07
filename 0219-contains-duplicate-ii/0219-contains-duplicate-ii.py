class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicts={}
        for i in range(len(nums)):
            if nums[i] in dicts:
                index = dicts[nums[i]]
                print(index)
                if abs(index-i)<=k:
                    return True
                else:
                    dicts[nums[i]] = i
            else:
                dicts[nums[i]] = i
        return False
            
            
                
        