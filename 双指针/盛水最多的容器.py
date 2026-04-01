def maxArea(self, height: List[int]) -> int:
  
        max_mianji=0
        for x in range(len(height)):
            for y in range(len(height)):
                mianji =min(height[x],height[y])*abs(x-y)
                max_mianji=max(max_mianji,mianji)
        return max_mianji
#这是我的原始思路，狠狠超时了，哭了