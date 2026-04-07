class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    #     bigest=nums[0]
    #     cur=nums[0]
    #    #nums=[91,-99,99，100]
    #    #nums[1:]=[-99,99,100]
    #     for x in nums[1:]:
    #         #第一次，x=-99,cur=91--->cur=-8
    #         #第二次，x=99,cur=-8---->cur=99
    #         #第3次，x=100,cur=99--->cur=199
    #         cur=max(x,cur+x)
    #         bigest=max(bigest,cur)
            
    #     return bigest

    #     #可以用DP欸

        f=[0]*len(nums)
        f[0]=nums[0]
        for i in range(len(nums)-1):
            f[i+1]=max(f[i],0)+nums[i+1]

        return max(f)










