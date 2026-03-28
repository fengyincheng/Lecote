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



#46. 全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #我要用队列吗？用队列的话...em..先所有元素加入队列，选择一个数字后把那个数字取出，再选另一个数》.....直到我取出所有元素为止。然后再把所有元素加入队列重选一遍。我可以规定一个一个来，比如以1，2，3开头后面都会有很多树节点。但是有树节点了其实我会更喜欢dfs。该怎么写呢？首先我用dfs的话，前一次的选择是会对之后的选择产生影响的，其次我怎么能设计算法决定每次选排列时选谁呢？
        
        n= len(nums)
        path=[0]*n 
        on_path=[0]*n 
        ans=[]
        def dfs(i: int):
            if i ==n:
            #应该是到最后一个树节点的末枝了，但是按索引来看不应该是n-1的位置吗
            #并非如此，意思是所有的答案都已经到了path这个数组中，可以添加到ans了。
            #最后一个索引是n-1那么到n不就是所有都写完了吗。
                ans.append(path.copy()) 
                #看不懂copy函数。：
                #好像是出于避免path的值被覆盖出现紊乱的问题。
                #因为path的更新方式不是重置而是更新？path是流动的。
                return
            for j, on in enumerate(on_path):  
                
                #nums = [10, 20, 30]
                #enumerate的用法：
                # for i, x in enumerate(nums):
                #     print(i, x) i会是索引，x会打印数组值。
                #所以这里j是索引。on是数组值
                if not on: #-->if on==False-->if not FALSE--->True 进入if
                           #-->if on==True--->if not True-->Fales 不进入if
                           #起到判断到底用还是没用过的作用。
                    path[i]=nums[j]  
                    
                    on_path[j]=True
                    dfs(i+1)
                    on_path[j]=False #回溯
                    # path不需要重置，path是流动更新的(path[i]=nums[j])。
        dfs(0)
        return ans


        