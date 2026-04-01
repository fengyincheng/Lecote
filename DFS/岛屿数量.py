#200. 岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0

        def dfs(x,y):
            
            if x<0 or x>=m or y<0 or y>=n:
                return
            if grid[x][y]=="0":
                return
            
            grid[x][y]="0"
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    res+=1
        return res   