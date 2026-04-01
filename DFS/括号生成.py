class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #核心是右括号数不得超过左括号数。可以设计左括号数始终大于等于右括号数。思路来源于灵山茶府。那么剩下的就是怎么插入的问题了。该如何插入括号而又不重复呢？
        path=['']*(n*2)  #如果n=3,那么依题意，就要有三队括号，也就是总计六个括号，也就是2N
        ans=[]

        def dfs(left,right):
            if right==n:
                ans.append(''.join(path))
                return

            if left< n:
                #path[left+right]='(' 
                #?不懂，为什么--->
                #比如left=1，right=0。
                #想当于往后插入。0的索引都已经有位置了
                #接下来填入新的括号就往后填，也就是索引left+right=1，索引一。
                path.append('(')
                dfs(left+1,right)
                path.pop()
            if right<left:
                #path[left+right]=')'
                path.append(')') 
                dfs(left,right+1)
                path.pop()
        dfs(0,0)
        return ans

        