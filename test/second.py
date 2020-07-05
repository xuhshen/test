# a= [1,2,3,[1,2,3,"a"] ]   
# 
# b=[a,"a"]
# 
# 
# print(b[0])
# 
# print("abchsf"[0])


a={
        "key1":1,
        "key2":2,
        "key3":[1,2,3],
        "key4":(1,2),
#         "k[]e_y5":"sdfsdf",
#         (1,2) :"dsfsd"
        
        }

# print(sorted(a.keys())) #对字典键值进行排序
# 
# print(a.keys())     #打印字典的键值
# print(a.values())   #打印字段的值
#  
# print(a.items())    #打印字段的键值对
# 
# print(a["key1"])
# print(a)

a["aaaaa"] = 657567
del a["key1"]


# {'aaaaa': 657567, 'key4': (1, 2), 'key2': 2, 'key3': [1, 2, 3, 4]}
print(a)




