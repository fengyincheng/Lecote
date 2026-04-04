class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charMaxRightIndex = {}

        for i,char in enumerate(s):
            charMaxRightIndex[char]=i
            #添加和覆盖字典。一个一个遍历即可得到每个字母在最右侧的索引
        # last = {
        #   'a': 2,
        #   'b': 1,
        #   'c': 3
        # }
        cur_right=0
        prev_indexx=-1  
        res=[]
        for i ,char in enumerate(s):
            cur_right = max(cur_right,charMaxRightIndex[char]) #char-->key
            if i == cur_right:
                res.append(i-prev_indexx) #你自己枚举一下就知道了，这道题要返回的是长度
                prev_indexx= i            #包括这里为什么要更新也跟返回值有关，很好理解吧
        return res
        #至于为什么不能像我下面的注释一样，用next_right来更新cur_right，
        # 是因为我要返回的长度是实时的，所以我要按新值更新，返回长度之前，cur_right必须更新。
        # 而跳跃游戏是存在滞后的，甚至按照建桥模型还可能回退，但是这里不需要回退，你懂我的意思吗？

        # next_right=0
        # for i,char in enumerate(s):
        #     next_right=max(next_right,charMaxRightIndex[char])
        #     if i==cur_right:
        #         cur_right=next_right
        #         res.append(i-prev_indexx)
        # return res



        