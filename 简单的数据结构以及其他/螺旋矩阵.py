matrix = [[1,2,3],[4,5,6],[7,8,9]]
def ZERO(matrix):
    if not matrix:
        return []
    left,right=0,len(matrix)
    top,botton=0,len(matrix[0])
    arr=[]
    while left<=right and top<botton:
        for c in range(left,right+1):
            arr.append(matrix[top][c])
            top+=1
        for x in range(top,botton+1):
            arr.append[x][right]
            right-=1
            



