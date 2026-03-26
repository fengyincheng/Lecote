# s = "cbaebabacd"
# p = "bac"
# left=0
# window_len = len(p)
# key="".join(sorted(p))
# # print(key)
# container=[]
# for ide in range(len(s)-window_len+1):
#     window=s[ide:ide+window_len]
#     #s[a:b] 代表从 a 开始，到 b 结束，但不包含 b 的那个位置。
#     if key=="".join(sorted(window)):
#         container.append(window)
# print(container)
# print(len(container))

#更不容易超时的正解

s = "cbaebabacd"
p = "bac"

window=[0]*26
left=0
key_window=[0]*26
count=0
result=[]
for i in p:
    count=ord(i)-ord('a')
    key_window[count]+=1
for right in range(len(s)):
    right_str=s[right]
    
    window[ord(right_str)-ord('a')]+=1
    while (right-left)>=len(p):
        window[ord(s[left])-ord('a')]-=1
        left+=1
    
    if window==key_window:
        result.append(left)
print(result)



    




    