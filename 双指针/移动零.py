class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums = [0,1,0,3,12]
        for number in nums:
            if number ==0 :
                nums.remove(number)
                nums.append(0)
        #以下是进阶操作：(双指针)
        # 把所有非 0 的数，按原顺序，往数组前面“挤”；
        # 后面剩下的位置，自然就全是0
        show = 0
        for i in range(len(nums)):
            #遍历数组的索引，不是值或者说元素
            if nums[i] !=0:
                nums[show],nums[i] = nums[i],nums[show]
                #依据索引交换位置，我也是第一次知道还可以这样写
                show +=1