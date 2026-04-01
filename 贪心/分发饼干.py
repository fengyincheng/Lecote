class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        count=0
        ren=0
        binggan=0
        while ren<len(g) and binggan<len(s):
            if g[ren]<=s[binggan]:
                ren+=1
                count+=1
            binggan+=1

        return count

        