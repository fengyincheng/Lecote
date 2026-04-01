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
    


        # table={0:1}
        # totally=0
        # count=0
        # for x in nums:
        #     totally+=x
        #     if totally-k in table :
        #         count+=1*table[totally-k]
                

        #     table[totally]=table.get(totally,0)+1  #如果value存在，返回value，如果value不存在，返回0
        # return count



        # N=len(nums)
        # preSum=[0]*(N+1)
        # for i in range(N):
        #     preSum[i+1]=preSum[i]+nums[i]
        # right=len(nums)-1
        # left=0
        # quchong=()
        # while left<right:
        #     normul=preSum[right+1]-preSum[left]
        #     if normul==k:
        #         table=[]
        #         for i in range(left,right+1): #终点不包含
        #             table.append(i)
        #         quchong.append(table)
        #     left+=1
        #     right-=1
        # for z in nums:
        #     if z == k:
        #         quchong.append(z)

        # totally=len(quchong)
        # return totally   
                 

        
