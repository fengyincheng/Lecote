class Solution:
    def rob(self, nums: List[int]) -> int:
        N=len(nums)
        dp=[0]*(N+1)
        #有N间房子，偷N间房子能得到的最大金额--->（有n-1间房子时偷盗的最大金额且没有偷最后一间房子）f(n-1) or f(n-2)(偷n-2间房子时得到的最大金额且偷最后一间房子)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,N+1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[N]
