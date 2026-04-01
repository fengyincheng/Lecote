

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        MAPPING=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
       #MAPPING=[0,  1,  2,    3,    4,    5,    6,     7,    8,    9]
        n=len(digits)
        if n == 0:
            return []
        ans=[]
        path=['']*n
        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i]=c 
                #?上面是在干嘛呢？开始看不懂了。我好像又有点会了。好烦，脑子好难受
                dfs(i+1)
        dfs(0)
        return ans