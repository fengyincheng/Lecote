i=0
nums = [1,2,3,4,5,6,7]
k=3
nums=nums[::-1]
while i <k:
    x=nums.pop(0)
    nums.append(x)
    i+=1
print(nums)
nums=nums[::-1]
print(nums)
###以下实现原地修改，以上创建了新列表
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        self.reverse(nums)
        
        while i <k:
            x=nums.pop(0)
            nums.append(x)
            i+=1
        self.reverse(nums)
       
    def reverse(self,nums):
        l=0
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

#以下是最终版本，实现全部操作都使用reverse函数,规避pop(0)的时间复杂度过高问题

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.   

        """
        k=k%len(nums)
        self.reverse2(nums,0,len(nums)-1)
        self.reverse2(nums,0,k-1)
        self.reverse2(nums,k,len(nums)-1)
    def reverse2(self,nums,l,r):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
    
        
