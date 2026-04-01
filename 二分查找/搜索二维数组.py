class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #一眼单调递增把所有行排排站都递增，我能不能把他们并称一行然后二分查找呢？
        large=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                large.append(matrix[i][j])
        right=len(large)
        left=0
        while left<right:
            mid=(left+right)//2
            if target>large[mid]:
                left=mid+1
            else:
                right=mid
       
        if left<len(large) and large[left]==target:  #防止越界，即target很大，然后mid走到了索引len(large)的情况
            return True
        else:
            return False

        