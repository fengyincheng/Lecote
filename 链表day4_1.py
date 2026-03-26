import sys

n=int(sys.stdin.readline())
res=[0]+list(map(int,sys.stdin.readline().split()))
visted=[0]*(n+1)
cur=1 #环的起点
cnt=0 #当前步数
while True:
    # cnt+=1
    # if visted[cur]!=0:
    #     start=cur
    #     length=cnt - visted[cur]
    #     print(start,length)
    #     break
    # visted[cur]=cnt
    # cur=res[cur]
    cnt+=1
    if visted[cur]!=0:
        break
    visted[cur]=cnt
    cur=res[cur]
