class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums) 
 #假设有六个元素，就有索引0-5，而这里不减一和索引对齐是因为后续真正访问数组的是mid,而mid可能等于left但是mid永远小于right所以为了让mid在访问的时候不漏索引，这里不减一，让right比最大索引大一位
        while left<right:
            mid=(left+right)//2
            if target>nums[mid]:
                left=mid+1  
#为什么要加一呢 ——>因为left是有可能等于mid的如果出现了这种话情况mid在执行这条语句的时候left=mid就无效了，起不到缩小区间的作用，会导致死循环。
            else:
                right=mid
        return left
        