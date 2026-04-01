class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N=len(candidates)
        path=[]
        ans=[]
        if N==0:
            return []
        def dfs(candidates,begin,N,path,ans,xtarget):
            if xtarget==0:
                ans.append(path.copy())
                return
            if xtarget<0:
                return
            for i in range(begin,N):
                #path1=path+[candidates[i]]
                path.append(candidates[i])
                #dfs(candidates,i,N,path+[candidates[i]],ans,xtarget-candidates[i])
                
                dfs(candidates,i,N,path,ans,xtarget-candidates[i])
                path.pop()
        dfs(candidates,0,N,path,ans,target)
        return ans
        

        
        