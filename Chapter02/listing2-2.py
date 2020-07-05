# # Split up a URL of the form http://www.something.com
# 
# url = input('Please enter the URL:')
# 
# 
# 
# start = False # 标记是否要收集字符
# 
# tmp = [] #存放收集的字符
# 
# for aaa in url: #对字符串进行每个字符循环一遍
#     print(aaa,start)  
#     if aaa == "w":    #判断当前字符是否符合开始收集条件
#         start = True  # 当当前字符符合收集条件条件时，把标记修改为要收集字符
#     elif start == True and aaa == "/":  #当当前的标记为收集状态，同时检测到结束符
#         break   #退出当前循环
#         
#       
#     if start == True:  #标记状态为收集状态
#         tmp.append(aaa)  #把当前字符加到缓存变量里
# 
# print(start)
#         
# print(tmp)        
# print("_".join(tmp))


# ##############################
# for i in [1,2,3,4,5,6]:
#     pass
# 
# ##############################
# a = 1
# if a :
#     print(1)
# else:
#     print(a)
#     
#  ->a=[1,2,3,4,5,6,7,8,9,10]

a = [1,2,4,3,5]

# a=[1,2,3,4,5] ===>[5,4,3,2,1]
        
# print(a[::-1]   )  

a=a[::-1]   
print(a)



