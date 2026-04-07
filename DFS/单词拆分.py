class Solution:
    #难的相似
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len=max(map(len,wordDict))
        word=set(wordDict)
        @cache
        def dfs(i):
            if i ==0:
                return True
            for j in range(i-1,max(i-max_len-1,-1),-1):
                if s[j:i] in word and dfs(j):
                    return True
            return False

        return dfs(len(s))
        