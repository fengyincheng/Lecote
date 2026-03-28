#303. 区域和检索 - 数组不可变

class NumArray:

    def __init__(self, nums: List[int]):
        N=len(nums)
        self.preSum=[0]*(N+1)
        for i in range(N):
            self.preSum[i+1]=self.preSum[i]+nums[i]
        #前缀和基本模板
        

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1]-self.preSum[left]
        #计算区间【left,right】的和，拆分
        




