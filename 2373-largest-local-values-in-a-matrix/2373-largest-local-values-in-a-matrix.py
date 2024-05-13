class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        final = []
        
        size = len(grid)
        for i in range(size-2):
            maxi=[]
            for j in range(size-2):
                maxi.append(self.maxofgrid(grid, i, j))
            final.append(maxi)
        return final
    
    def maxofgrid(self, grid, x,y):
        maxi = 0
        for i in range(x,x+3):
            for j in range(y,y+3):
                maxi = max(maxi, grid[i][j])
        return maxi