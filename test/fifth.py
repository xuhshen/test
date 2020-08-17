import csv
import os


class people(object):
    def __init__(self,f=""):
        self.filename = f
        self.outputfolder = "result"
#         os.mkdir(self.outputfolder) 
        self.fields = []
        self.data = []
        self.cleandata = []
    
    def readcsvinfo(self):
        with open(self.filename,'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.fields = next(csvreader)
         
            for row in csvreader:
                self.data.append(row)
    
    def getcleandata(self):
        '''把不是 “地址” 开头的地址，过滤掉
        '''
        for data in self.data:
            if "地址" not in data[4]:
                pass
            else:
                self.cleandata.append(data)
        
        print(self.cleandata)
    
    def fenlei(self):
        '''根据地址，对人进行分类
          {"地址1"：[[...],[...]],
          "地址2"：[[...],[...]]}
        ''' 
        self.result = {}
        for data in self.cleandata:
            addr = data[4]  
            if self.result.__contains__(addr):
                self.result[addr].append(data)
            else:
                self.result[addr] = [data]
        
        print(self.result)      
    
    def ouptput(self):
        '''把分类后的结果，分别进行保存
        
        '''
        for k,v in self.result.items():
#             filename = self.outputfolder + k +".csv"
            filename = "{}/{}.csv".format(self.outputfolder,k)
        
            with open(filename,'w',newline = "") as csvfile:
                csvwriter = csv.writer(csvfile)
             
                #写入字段
                csvwriter.writerow(self.fields)
                 
                #写入行数据
                for item in v:
                    csvwriter.writerow(item)
        
    
    def setname(self):
        pass
    
    def getnamelist(self):
        pass
    
if __name__=="__main__":
    # filelist = ["info1.csv","info.csv"] 
    # for f in filelist:
    p = people("info.csv")
    p.readcsvinfo()
    p.getcleandata()
    p.fenlei()
    p.ouptput()


