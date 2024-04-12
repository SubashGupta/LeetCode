class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n
        right=[0]*n
        h=0
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        right[n-1]=height[n-1]
        for j in range(n-2,-1,-1):
            right[j]=max(right[j+1],height[j])
        print(left,right)
        for i in range(n):
            h+=min(left[i],right[i])-height[i]
        return h