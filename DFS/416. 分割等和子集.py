from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        # f=[0]*n
        # f[0]=nums[0]
        # for i in range(1,n):
        #     f[i]=f[i-1]+nums[i]
        #     count=sum(nums)
        #     if f[i] == count-f[i]
        Sum=sum(nums)
        if Sum%2 !=0:
            return False
        target=Sum//2
        @cache
        def dfs(i,c):
            if i < 0:
                if c==target:
                    return True
                else:
                    return False
            if c<target:
                return False
            
            return dfs(i-1,c-nums[i]) or dfs(i-1,c)
            # 我的c表示没选的和。而且我觉得
                # if i < 0:
                    # if c==target:
                    # return True
                # else:
                    # return False   
             # 没关系，因为都已经选到最后一个和了，如果要返回true那没选的肯定要等于选了的等于总和的一半，不然就错了。
             # 而且 dfs(i-1,c-nums[i]) dfs(i-1,c)这两个根本没必要return。
             # 因为我本来就是想让她们选到最后一个，也就是i<0的情况，本来我就打算用递归入口做return的。
             # 之前图论，我dfs初入门那里我就是这样写的
            """
            但问题是：

            子递归 return 的值不会自动传给父递归。
            dfs(2,7)   # 算完丢掉
            dfs(2,10)  # 算完丢掉
            因为图论 DFS 很多时候是：

            visited.add(x)
            dfs(nei)

            你：

            不关心 dfs 的返回值

            只是利用递归：

            去遍历 / 标记 / 修改外部变量
            """
            # return dfs(i - 1, c - nums[i]) or dfs(i - 1, c)
            # 要是前面false了后面是True怎么办
            """
            不会有问题，因为 Python 的 or 语义正是：

            A or B

            表示：

            只要 A / B 有一个为 True，整个结果就是 True
            """
        return dfs(n-1,Sum)


