class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 背包问题的变种。就是打家劫舍改一下，你自己看吧
        n=len(coins)

        @cache
        def dfs(i,c):
            if i<0:
                if c==0:
                    return 0
                else:
                    return float('inf')
                    #无穷大
            if c<0:
                return float('inf')
            res=min(dfs(i,c-coins[i])+1,dfs(i-1,c))
            return res
        totally = dfs(n-1,amount)
        if totally == inf:
            return -1
        else:
            return totally
        