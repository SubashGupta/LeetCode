class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        j=len(nums)-1
        i=0
        op=[]
        while i<=j:
            if abs(nums[i])<abs(nums[j]):
                op.append(nums[j]*nums[j])
                j-=1
            else:
                op.append(nums[i]*nums[i])
                i+=1
        return op[::-1]
                    
            
            
        