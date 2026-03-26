# 733. 图像渲染
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original= image[sr][sc]
        if original==color:
            return image
        row=len(image)
        cols=len(image[0])

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=cols:  #防止越界
                return
            if image[r][c] !=original:
                return #不符合染色条件
            image[r][c] = color

            dfs(r+1,c) #向上
            dfs(r,c+1) #向下
            dfs(r-1,c) #向左
            dfs(r,c-1) #向右
        dfs(sr,sc)
        return image
    
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
