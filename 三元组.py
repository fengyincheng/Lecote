class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    #先来看看我的蠢人代码，绷不住一点
        left=0
        right=len(nums)-1
        is_sanyuanzu=[]
        while left < right:
            nums_start=nums[left]
            nums_end=nums[right]
            three=abs(0-(nums_end+nums_start))
            if three in nums:
                new_nums=[nums_start,nums_end,three]
                is_sanyuanzu.append(new_nums)
            if three>0:
                #数偏大了？
                if nums_end > nums_start:
                    right-=1
                else:
                    left+=1
            if three<0:
                if nums_end >nums_start:
                    left+=1
                else:
                    right-=1   


#以下是正解：     
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        
        new_nums=sorted(nums)
        n = len(new_nums)
        result=[]
        
        while i<n-2:
            if i>0 and new_nums[i]==new_nums[i-1]:
                i+=1
                continue
            left=i+1
            right=len(nums)-1
            one=new_nums[i]
            
            while left < right:
                two=new_nums[left]
                three=new_nums[right]
                if one +two +three ==0:
                    container=[one,two,three]
                    result.append(container)
                    while left < right and new_nums[left] == new_nums[left+ 1] :
                        left+=1
                    while left < right and new_nums[right] == new_nums[right-1] :
                        right-=1
                    left += 1
                    right -= 1

                else:
                    if -one<(two+three):
                        #pian da
                        right -=1
                    if -one>(two+three):
                        left+=1

            i+=1
        return result
    
#思路挺简单的，难的是去重，三次去重，我真的