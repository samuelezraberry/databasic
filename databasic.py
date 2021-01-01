import os
import csv
class table:
    def __init__(self, path):
        self.file_name=path

    def getColumn(self,column):
        f=open(self.file_name,"r")
        lines=f.readlines()
        columns=[]
        for line in lines:
            lineSplit=line.split("|") # split the line over the divider character
            if lineSplit[0]==column:
                data="|".join(lineSplit[1:]).strip("\n") # data is everything after the first "|" in the string
                try:
                    data=int(data) # try to parse the data as integer, else keep as string
                except:
                    pass
                columns.append(data)
        f.close() # close the file
        return columns

    def columnSize(self,column):
        return len(self.getColumn(column))

    def append(self,column,content):
        with open(self.file_name, 'a') as f:
            f.write(column+"|"+content+"\n")

    def destroy(self):
        os.remove(self.file_name)

    def overwrite(self,fullTable):
        headers=self.headers()
        with open(self.file_name, 'w') as f:
            for i in range(len(fullTable)):
                h=headers[i]
                for row in fullTable[i]:
                    f.write("{0}|{1}\n".format(h,row))

    def remove(self,column,itemIndex):
        fullTable=self.readTable()
        columnIndex=self.headers().index(column)
        del fullTable[columnIndex][itemIndex]
        self.overwrite(fullTable)

    def headers(self):
        f=open(self.file_name,"r")
        lines=f.readlines()
        columns=[]
        for l in lines:
            ls=l.split("|")
            if ls[0] not in columns:
                columns.append(ls[0])
        f.close()
        return columns

    def readTable(self):
        fullTable=[]
        for h in self.headers():
            fullTable.append(self.getColumn(h))
        return fullTable

    def longestColumn(self):
        n=0
        longestLen=0
        longestColumn=0
        for col in self.readTable():
            l=len(col)
            if l>longestLen:
                longestLen=l
                longestColumn=n
            n+=1
        return self.headers()[longestColumn]

    def exportCSV(self,outfile):
        f=open(outfile,"w")
        headers=self.headers()
        fullTable=self.readTable()
        with open(outfile, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            longest=len(self.getColumn(self.longestColumn()))
            writer.writerow(headers)
            for i in range(longest):
                row=[]
                for c in fullTable:
                    try:
                        row.append(c[i])
                    except:
                        row.append("")
                writer.writerow(row)
