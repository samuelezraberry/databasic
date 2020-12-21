# databasic
_structured data management using text files_


[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=E5BUE63ZUWDHS&source=url)

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
