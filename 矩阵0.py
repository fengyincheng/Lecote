matrix = [[1,1,1],
          [0,0,1],
          [1,1,1]]

lie_extinct_zero=False
m=len(matrix)
n=len(matrix[0])
for i in range(m):
    
    if matrix[i][0]==0:
        matrix[0][0]=0
        break
for i in range(n):
    
    if matrix[0][i]==0:
        lie_extinct_zero=True
        break
#以上判断第一行和第一列是否有0，并做标记

for i in range(1,m):
    for j in range(1,n):
        if matrix[i][j]==0:
            matrix[i][0]=0
            matrix[0][j]=0
#以上遍历除了第一行和第一列的元素，遇到0时做标记

for i in range(1,m):
    if matrix[0][i]==0:
        for j in range(n):
            matrix[0][j]=0
#以上判断第一行是否有0，如果有，将对应列置0
for i in range(1,n):
    if matrix[0][i]==0:
        for j in range(m):
            matrix[j][0]=0
#以上判断除了第一列的第一个元素外的第一列是否有0，如果有，将对应行置0

if lie_extinct_zero==True:
    for i in range(m):
        matrix[i][0]=0

#以上单独判断第一列是否有0，如果有，将第一列置0

if matrix[0][0] == 0:
    for j in range(n):
        matrix[0][j] = 0
           
