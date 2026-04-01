#695. 岛屿的最大面积
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        def dfs(x,y):
            
            if x<0 or x>=m or y<0 or y>=n:
                return 0
            if grid[x][y] != 1:
                return 0
            grid[x][y]=0
            mianji=1
            mianji += dfs(x+1,y)
            mianji += dfs(x-1,y)
            mianji +=dfs(x,y+1)
            mianji +=dfs(x,y-1)
            return mianji 
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count=max(count,dfs(i,j))
        return count        
