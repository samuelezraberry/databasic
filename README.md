# databasic
_Simple, light weight, and versatile data management system for Python_

---

## example of use

```
import databasic as dbsc

myNewTable=dbsc.table("mynewtable")

# write random items to column "things"
myNewTable.write("things","apple")
myNewTable.write("things","banana")
myNewTable.write("things","cat")

myNewTable.read("things")
# returns ['apple', 'banana', 'cat']

myNewTable.write("colours","green")
myNewTable.write("colours","yellow")
myNewTable.write("colours","black")

myNewTable.columns()
# returns ['things','colours']

myNewTable.length('things')
# returns 2

print(myNewTable.read("things")[0],myNewTable.read("colours")[0])
# prints "apple, green"

myNewTable.remove("things",1)
myNewTable.read("things")
# returns ['apple','cat']

myNewTable.destroy()
# deletes table

```
