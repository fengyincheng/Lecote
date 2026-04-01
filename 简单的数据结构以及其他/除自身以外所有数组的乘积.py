#eg.nums = [1,2,3,4]
# return ans[2*3*4,1*3*4,1*2*4,1*2*3] = [24,12,8,6]
#可以理解为先求一个元素前缀积和后缀积，再把二者相乘，得到ans中数组的一个元素，也以此为思路求其他元素
#一开始想的是，用for遍历数组，再求每个元素的前缀和后缀积，但是这是无法同时在一个for循环中完成的
#那么可以分别求所有前缀积和后缀积，再对应相乘既可以了，不需要创建任何新数组，除了要return的目标数组ans本身
#可以先将前缀和存入ans中，再将后缀积乘到ans中,注意最左边的前缀积为1，最右边的后缀积为1
#注意后缀积的遍历方式


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        perfix=1
        for i in range(len(nums)):
            ans[i]=perfix
            perfix=nums[i]*perfix
        
        sunfix=1
        for i in range(len(nums)-1,-1,-1):
            #range(开始值，结束值[不包含],步长)
            ans[i]=ans[i]*sunfix
            sunfix=sunfix*nums[i]
        return ans



            