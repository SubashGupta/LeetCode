class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=0
        end=len(nums)-1
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                leftstart = mid
                rightend = mid
                while nums[leftstart-1] == target and leftstart>0:
                    leftstart-=1  
                while rightend < len(nums) - 1 and nums[rightend + 1] == target:
                    rightend+=1
                return [leftstart, rightend]
            elif nums[mid]<target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1,-1]