class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def erfen_left(nums,target):
            #开区间写法。被人推荐的，听说好记。以下大部分代码都参考灵山茶府
            right=len(nums)
            left=-1

            while left+1<right:
                mid=(left+right)//2
                if nums[mid] >= target :
                    right=mid
                else:
                    left=mid
            return right
        def erfen_right(nums,target):
            right=len(nums)
            left=-1
            while left+1<right:
                mid=(left+right)//2
                if nums[mid] <= target:
                    #注意这里跟找左边界不一样。
                    left=mid
                else:
                    right=mid
            return left #注意这里也不一样
        
        
        start = erfen_left(nums,target)
        #我第一个找的肯定是最左边的那个。这是因为我没有return mid所以我是找的左边界。之前写的左开右闭的写法也一样找的左边界。具体可以看35
        if start == len(nums) or nums[start] !=target:
            #处理越界和没找到的问题
            return [-1,-1]
        end = erfen_right(nums,target)
        
        return [start,end]
        

            