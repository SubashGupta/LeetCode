class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1:
                return 1
            elif grid[i][j] == 0:
                return 1
            elif grid[i][j] == -1:
                return 0
            else:
                grid[i][j] = -1
                return dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(i, j)