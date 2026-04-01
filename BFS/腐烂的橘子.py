from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # row=len(grid)
        # cols=len(grid[0])
        # times=0
        
        # def dfs(r,c):
        #     if r<0 or r>=row or c<0 or c>=cols:
        #         return
        #     if grid[r][c] != 2:
        #         return
        #     grid[r][c]=2
        #     nonlocal times+=1
        #     dfs(r,c+1)
        #     dfs(r+1,c)
        #     dfs(r-1,c)
        #     dfs(r,c-1)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]==2:
        #             dfs(i,j)
        # return times

        # #坏了，一开始想到自己可以用dfs写来着，怎么越写越不对劲呢
        
        q=deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
        row=len(grid)
        cols=len(grid[0])
        times=0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]  #四个方向
        while q:  #这算什么终止条件--->队列为空时停止
            size=len(q)  
            is_ganran=False
            for _ in range(size): #怎么遍历队列啊，不是很会，我都忘记怎么遍历list了
                x,y=q.popleft()   #实际上不需要遍历，取出来就行了

                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy  #神奇的

                    if 0<=nx <row and 0<= ny <cols and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        q.append((nx,ny))
                        is_ganran = True
            if is_ganran==True:
                times+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return times 

