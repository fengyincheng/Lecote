49
strs = ["eat","tea","tan","ate","nat","bat"]
group={}
for s in strs:
    key="".join(sorted(s))
    #eg.when s="eat",sorted(s) = ['a','e','t'],key="aet"
    if key not in group:
        group[key]=[]   #key对应key:value中的key,value对应一个空列表
        #group ={'aet':[]}
    group[key].append(s)  #通过取到字典里的列表，对该列表使用append方法,字典本身不能使用append方法
    #此时，group={'aet':['eat']}

#几轮for后：group={'aet':[aet,tea,eat]}                          
a =list(group.values())
print(a)


