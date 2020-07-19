# 
# def hello1(a,b,c=0):
#     
#     return sum(a)+b
# 
# # def hello2(a,b):
# #     pass
# #     
# arg = [1,2,3,4,5,6,7,8] 
# arg2 = 3
# 
# a1 = hello1(arg,arg2)
# 
# # a2 = hello2(1,2)
# 
# print(a1)
# 
# # print(a2)



# def find2(arg=[]):
#     tmp = []
#     for i in arg:
#         if i%2  == 0:
#             tmp.append(i)
#     
#     return tmp
# 
# 
# ##########################################
# a = [1,2,3,4,5,6,7,10,20,45]
# 
# print(find2(a))
#             
# 
# b = [10,8,4,20,70,5]   #找到大于10 的数字



# dct = {
#         "name1":{
#                 "phone":13586294819,
#                 "addr" : "address1"
#                 },
#        
#         "name2":{
#                  "phone":18856234915,
#                  "addr": "address2"
#                  }
#        }
# 
# def findinfo(name,key):
#     
#     if key == "phone":
#         return dct[name][key]
#     
#     elif key == "addr":
#         return dct[name][key]
#     
#     else:
#          return dct[name]
# 
# 
# print(findinfo("name1","phone"))
# 
# print(findinfo("name2","addr"))
# 
# print(findinfo("name2",""))


#问题1： 输入列表名字，返回列表里值的和
DCT = {
       "list1":[1,2,3,4,5],
       "list2":[7,8,9,20],
       "list3":[3,4,6,8,9],
       }

def getsum(key):
    try:
        tmp = DCT[key]
        return sum(tmp)
    except:
        return "key error!"



# print(getsum("list2"))

#问题2：把字典里，找到值值最大的那个键的名字
dct = {
       "key1":10,
       "key2":80,
#        "key3":16,
       "key4":5,
       "key5":80
    }


# def getmax(dct):
#     tmp = None
#     for k,v in dct.items():
#         if tmp is None:
#             key = k
#             tmp = v
#         elif tmp < v :
#             key = k
#             tmp = v
#     
#     return key
# 
# print(getmax(dct))


# f = open("example.txt",mode="r")
# print(f.read())

# store = {}

# import csv
# with open('../Chapter29/example.csv', 'r') as f:
#      reader = csv.reader(f)
# #      print(type(reader))
#     
#      for row in reader:
#          if row[0] != "name":
#              store[row[0]] = row[1]
#          print(row)
# 
# print(store)

#例子 : 输出明天是哪一年几月几号？

from datetime import datetime,timedelta 
 
# def gettomorrowdate():
#     now = datetime.now()
#     diff = timedelta(1)
#     print(now)
#   
# gettomorrowdate()

# print(datetime.today())
# 
# print(timedelta(-2))

today = datetime.today()-timedelta(0)
print(today.isoweekday())
 
# print(yestoday.strftime('%Y-%B-%d-%w %H:%M:%S' ))


def judgetoday(day):
#     now = datetime.now()
    
#     for i in range(20):
#         print((now-timedelta(-i)).weekday())
    
    week = day.isoweekday()
    if week in [6,7]:
        return 1
    else:
        return 0
    
#     print(week)


day = datetime.now()+timedelta(-0)


print(judgetoday(day))





