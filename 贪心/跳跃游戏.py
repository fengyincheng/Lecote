class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx=0
        for i,j in enumerate(nums):
            if i >mx:
                return False
            mx=max(mx,j+i)
        return True

        #私以为这道题真的很难想。怎么说呢？我是可以理解为什么这么做的，但是我现在说不太出来，说明我也没有会透，改天补一下。思路看的是灵神。

        