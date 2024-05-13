class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            if grid[i][0] == 0:
                #logic to flip
                for j in range(columns):
                    grid[i][j] = 1 - grid[i][j]
        
        for j in range(1, columns):
            c=0
            for i in range(rows):
                if grid[i][j] == 0:
                    c+=1
            if c > rows-c:
                for k in range(rows):
                    grid[k][j] ^= 1
        
        sums = 0
        for i in range(rows):
            x=''
            for j in range(columns):
                x+=str(grid[i][j])
            sums+=int(x,2)
        return sums