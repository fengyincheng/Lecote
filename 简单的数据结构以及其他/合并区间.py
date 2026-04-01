class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        container=[]
        cur=intervals[0]
        #intervals=[[1,3],[2,6],[8,10]]
        for x in range(1,len(intervals)):
            if cur[1] >=intervals[x][0]:
                cur[1]=max(cur[1],intervals[x][1])
                
            else:
                container.append(cur)
                cur=intervals[x]
        container.append(cur)
        return container