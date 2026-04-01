class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        #这里dp的含义是---》dp[i]以i结尾的最长子序列的长度。假设i=7球的就是以7结尾最长的子序列长度数
        for i in range(n):
            for j in range(i): #生成0~n-1的索引
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)  #有一种跟说好的不一样的被刺感。你把最长的递增子序列拆成了什么或什么的子问题呢？
        #以上的解释：还是以7为例，j是生成的随机索引会遍历索引7之前，也就是dp.0~6索引值的所有元素。其实做到这里更像之前需要用max更新的题目。反正通过if条件，最后dp[7]会得到以7结尾的最大子序列长度。
        return max(dp)
        