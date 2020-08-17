# def fun(a=[1,101]):
#     lst = range(a[0],a[1])
#     tmp = 0
#     for i in lst:
# #         tmp += i    
#         tmp = i + tmp
#     return tmp 
# 
# def compare(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#         
#  
# rst = fun([2,200]) 
# rst_new = compare(rst,5620)
#     
# print(rst_new)

#给定一个列表，把列表里能把被5 整除的数都找出来 
# def find138(a):
#     tmp=[]
#     for i in a:
#         print(i)
#         i = str(i)
#         print(i)
#         if "138" in i:
#             tmp.append(i)
#     return tmp
#         
# a=[138254135,655352138,137569843]    
# print(find138(a))
import csv

def inputnameandphone(name="小王",phone=135689534,filename="info.csv"):
    fields = []
    rows = []
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
     
        for row in csvreader:
            rows.append(row)
    
    print(fields,row)
    rows.append([name,phone])
    
    newrow = []
    for i in rows:
        if  i :
            newrow.append(i)
            
    print(newrow)
    with open(filename,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
     
        #写入字段
        csvwriter.writerow(fields)
         
        #写入行数据
        for item in newrow:
            csvwriter.writerow(item)
        
inputnameandphone("阿狗",121235456)

#  with open(filename,'a') as csvfile:
#         csvwriter = csv.writer(csvfile)
#      
#         #写入字段
# #         csvwriter.writerow(fields)
#          
#         #写入行数据
#         csvwriter.writerow(row)























