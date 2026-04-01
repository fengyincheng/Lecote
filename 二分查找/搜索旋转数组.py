class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=[]
        n=len(nums)-1
        index=0
        for i,j in enumerate(nums):
            if  nums[i-1]>nums[i]:
                index=i
                break
        def erfen(start,end):
            start-=1
            end+=1
            while start+1 < end:
                mid=(start+end)//2
                if nums[mid]>=target:
                    end=mid
                else:
                    start=mid
            if end < len(nums) and nums[end] == target:
                return end
            return -1
        
        one=erfen(0,index-1)
        two=erfen(index,len(nums)-1)
        if one != -1:
            return one
        if two != -1:
            return two
        else:
            return -1

        