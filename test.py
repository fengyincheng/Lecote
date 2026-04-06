res=[]
# n=10
# path='Q'*n
# print(f"{path}\n"*n)
# path.append([1])
# print(path)

# s="abc"
# i=len(s)
# print(i)
# continue
# x=1
# for i in range(1,10,-1):
#     print(i)
  

import os
import sys

# 请在此输入您的代码

ans=[]

for i in range(12345678,987654322):
  ans.append(i)
count=0
for j in range(len(ans)):
  Str=str(ans[j])
  target="2023"
  i=0
  for x in Str:
    if x==target[i]:
      i+=1
  if i==len(target):
    count+=1
    
  