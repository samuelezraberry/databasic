# databasic
_simple text file databse program_


## example of use

```
import databasic as dbsc

myNewTable=dbsc.table("mynewtable")

# write random items to column "things"
myNewTable.append("things","apple")
myNewTable.append("things","banana")
myNewTable.append("things","cat")

print(myNewTable.getColumn("things"))
# returns ['apple', 'banana', 'cat']

myNewTable.append("colours","green")
myNewTable.append("colours","yellow")
myNewTable.append("colours","black")

print(myNewTable.headers())
# returns ['things','colours']

print(myNewTable.columnSize('things'))
# returns 2

print(myNewTable.getColumn("things")[0],myNewTable.getColumn("colours")[0])
# prints "apple, green"

myNewTable.remove("things",1)

myNewTable.getColumn("things")
# returns ['apple','cat']

myNewTable.exportCSV("my.csv")
# exports to csv

myNewTable.destroy()
# deletes table

```
