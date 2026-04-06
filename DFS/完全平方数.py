from functools import cache
from math import inf, isqrt
@cache
def dfs(i,j):
    if i == 0:
        if j:
            return inf
        else:
            return 0
    if j<i*i:
        return dfs(i-1,j) #只能不选
    return min(dfs(i-1,j),dfs(i,j-i*i)+1)
class Solution:
    def numSquares(self, n: int) -> int:
        # isqrt（n）给n开根号，开出小数点就向下取整
        
        return dfs(isqrt(n),n)

        
        