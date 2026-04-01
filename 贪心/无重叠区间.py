class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1]) #eg.intervals[0]=[1,2]。x[1]-->[1,2][1]-->2。按索引1，也就是第二个元素的大小给各个区间排序。

        count = 1
        end = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0] >= end:
                count+=1
                end = intervals[i][1]

        return len(intervals)-count
        #现在你写的每行代码我都看的懂了，但你不理解你为什么这样写，也不理解你这样写为什么能达到目的。
 
        #首先sort后能够得到结束最早的，也就是尾端最小的区间。然后这道题的思想是得到结束最早的区间--->开始判断其它区间的首段，如果首段比前面的尾端要大，那么这个区间一定不会和上个区间重合，保留，更新end值，判断下一个区间，用相同的方法
        #为什么要先选尾端最小，也就是结束最早的--->因为结束早就越不可能跟其他区间冲突。比如[1,2] or[1,100]

        