#错误思路，我用的滑窗,好像是没考虑有负数的情况
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        container=[]
        # for i in nums:
        #     tantative=[]
        #     if i ==k:
        #         tantative.append(i)
        #         container.append(tantative)
        left=0
        right=0
        tantative1=[]
        for i in range(len(nums)):
            tantative=nums[left:right+1]
            key=sum(tantative)
            if key==k:
                container.append(tantative)
                tantative.clear()

            
            while key > k and left < right:
                left+=1
                tantative=nums[left:right+1]
                key=sum(tantative)
                if key==k:
                    container.append(tantative)
                    tantative.clear()
            right+=1
        count =len(container)
        return count