class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        s:所有数之和
        p:所有要取正数的数之和
        s-p:所有要取负数的数之和（题目限制数组里的都是正数。
          #注意这里是要去，还没取，p是正数）
        t=p-(s-p)
        p=(t+s)/2
        故s+t必须为偶数，因为p一定是整数,所以s+t要能被2整除。
        s+t也必须是正数，因为p>0

        """
        #我们先把s+t算出来
        target=target+sum(nums)
        if target<0 or target%2 !=0:
            return 0
        target=target//2
        #到这里我们已经把p求出来了
        #然后现在的问题就变成了，我在nums数组里选或不选一个数
        #然后我选中的数何时相加等于p的问题了。
        # 就变成了打家劫舍的dfs版的改动版。
        @cache
        def dfs(i,c):
            if i< 0:
                if c==0:
                    return 1
                    #找到一种方案，返回1
                else:
                    return 0
            res=dfs(i-1,c-nums[i])+dfs(i-1,c)
            return res
        n=len(nums)
        return dfs(n-1,target)

        
            
        