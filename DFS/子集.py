class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # N=len(nums)
        
        # on_path=[False]*N 
        # ans=[[]]
        # def dfs(i: int,path: List):
            
        #     if i ==N:
        #         ans.append(nums)
        #         return
        #     for j,on in enumerate(on_path):
        #         if not on:
        #             path.append(j)
        #             ans.append(path)
        #             on_path[j]=True
        #             dfs(i+1,path)
        #             on_path[j]=False
        # dfs(0,[])
        # return ans
        ans=[]
        def dfs(start,path):
            ans.append(path[:]) #那为什么不写append(path)
            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop() #回溯

        dfs(0,[])
        return ans




        