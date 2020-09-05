import os
class table:
    def __init__(self, table_name):
        self.tabe_name=table_name
        self.file_name=table_name+".dbs"
        with open(self.file_name, 'a'):
            pass

    def read(self,column):
        f=open(self.file_name,"r")
        lines=f.readlines()
        columns=[]
        for l in lines:
            ls=l.split("|")
            if ls[0]==column:
                x=ls[1].strip("\n")
                try:
                    x=int(x)
                except:
                    pass
                columns.append(x)
        f.close()
        return columns

    def length(self,column):
        return len(self.read(column))

    def write(self,column,content):
        try:
            column=sanitize(column);content=sanitize(content)
            with open(self.file_name, 'a') as f:
                f.write(column+"|"+content+"\n")
            return True
        except:
            raise
            return False

    def destroy(self):
        os.remove(self.file_name)

    def remove(self,column,index):
        rows=self.read(column)
        fr=open(self.file_name,"r")
        r=fr.read()
        r=r.replace(column+"|"+rows[index]+"\n","")
        with open(self.file_name,"w") as f:
            f.write(r)
        return True

    def columns(self):
        f=open(self.file_name,"r")
        lines=f.readlines()
        columns=[]
        for l in lines:
            ls=l.split("|")
            if ls[0] not in columns:
                columns.append(ls[0])
        f.close()
        return columns

def sanitize(s):
    return str(s).replace("|","¦")
