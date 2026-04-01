class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = [100,4,200,1,3,2,0,0,2]
        nums_set = set(nums)
        #nums_set = {100,4,200,1,3,2,0}
        long = 0
        for y in nums_set:
            
            if y-1 not in nums_set:
                a = y
                count = 1
                while a+1 in nums_set:
                    count +=1
                    a += 1
                long =max(long,count) 
        return long 
        