class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res=nums[0]
        # for i in range(1,len(nums)):
        #     res=max(res,res*nums[i])
        # return res
        f_min=[0]*len(nums)
        f_max=[0]*len(nums)
        f_min[0]=nums[0]
        f_max[0]=nums[0]
        # 我们需要判断有负数的情况。但我不想区分怎么办？
        # 假设x=nums[i],如果是一路正数，那么就是最普通的情况。
        # 如果存在负数，那假设x是个负的，那下一个是负的那么直接负负得正。
        # 怎样最大呢？f_min[i]最小乘积有可能遇到下一个负数直接得正变成最大。
        # 所以我们需要最小乘积解决负数的情况。
        # 同时也要存在最大乘积，因为我们最后要提交的是最大乘积，最小乘积的存在是为了得到最大乘积。
        # 同时注意f_max和f_min的顺序问题。因为最大乘积要用f_min的上一个状态，所有min要后更新
        for i in range(1,len(nums)):
            f_max[i]=max(f_max[i-1]*nums[i],f_min[i-1]*nums[i],nums[i])
            f_min[i]=min(f_max[i-1]*nums[i],f_min[i-1]*nums[i],nums[i])

        return max(f_max)