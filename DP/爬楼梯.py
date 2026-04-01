class Solution:
    def climbStairs(self, n: int) -> int:
     
        # def dfs(remain):
        #     if remain==0:
        #         return 1
        #     if remain<=0:
        #         return 0
        #     return dfs(n-1) + dfs(n-2)
        # return dfs(n)
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1  #为什么01的要设定成1？--->dp[n]的核心含义是从n道0需要的方法。dp[0]已经在终点方法1。dp[1]离终点还有一步只能走1方法1.
        for i in range(2,n+1):  #为什么要从索引二开始算？-->因为i需要大于等于2
            dp[i]=dp[i-1]+dp[i-2]
        #类似递归的逆过程，疑似递归的本质。
        return dp[n]    
            
            
        