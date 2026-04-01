class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]

        for i in range(numRows):
            row = [1] * (i+1)
            #利用双循环边生成边处理
            for j in range(1,i):
                row[j]=res[i-1][j-1]+res[i-1][j]
                #可是前两行不需要处理啊，三个1，而我没有看见你考虑了这一点
            
            res.append(row)

        return res
        