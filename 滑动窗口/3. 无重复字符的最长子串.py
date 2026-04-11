
s = "abcabcbb"
max_len=0
n =len(s)

for i in range(n):
    current_len=0
    set_chars=set()
    for j in range(i,n):
        
        if s[j] in set_chars:
            break
        else:
            set_chars.add(s[j])
            current_len+=1
    max_len=max(max_len,current_len)
print(max_len)
#上面这些都是按我自己一开始的思路想出来但又没做出来，是gpt帮我改的
#以下是滑动窗口：
s2 = "adcdsad"
buchongfu_str = set()
left = 0
#定义left为全局变量是因为她像个指针一样从索引0开始动。怎么动呢？循环里加一相当于右移了
max_length = 0
for right in range(len(s2)):
    #假设已经过了三轮for循环，现在集合里有adc
    #第四轮开始了，现在s2取到d,重复了，符合while条件，进循环了
    
    while s2[right] in buchongfu_str:
        #把左指针指向的字符删掉，直到里面没有d为止
        buchongfu_str.remove(s2[left])
        left += 1
        #删了两次了，集合里就变成了c，退出while
    buchongfu_str.add(s2[right])
    #可以添加新字符了，d进了，后面如果还不重复接着加，但在加之前要更新最大长度
    #万一又要删了，这组合长度就没了，所以可能没之前记一下
    max_length = max(max_length, right - left + 1)
print(max_length)