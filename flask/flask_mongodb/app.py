from flask import Flask
import flask
from flask_pymongo import PyMongo

app=Flask("mongoapp")
app.config["MONGO_URI"] = "mongodb://localhost:27017/mymongodb"

# ORM
mongo = PyMongo(app)
db=mongo.db

'''
#CREATE
db.mycoll.insert_one({'name':'rahul', 'roll_no':182056})   #creates a table mamed mycoll and insert one entry
db.mycoll.insert_many([{'name':'jack', 'roll no':1},
                      {'name':'robert', 'roll no':2}])     # creates multiples entries in the collection mycoll. 
'''


'''
#READ
output=db.mycoll.find_one({'roll no':1})
print(output)

output=db.mycoll.find()
for i in output:
    print(i)                                                                # this will print all the entries with the help of loop
'''

'''
#UPDATE
myquery = { "roll no": 1 }
newvalues = { "$set": { "name": "jack" } }              

x=db.mycoll.update_many(myquery, newvalues)                                # update_many will update all the entries. use update_one if you want to update the intitial entry only.
print(x.modified_count, "document updated")
'''


'''
#Delete
myquery={'roll no':1}
db.mycoll.delete_one(myquery)                               # deletes an entry where roll no is 1
'''
'''
x = db.mycoll.delete_many({})
print(x.deleted_count, " documents deleted.")               # deletes the whole collection and prints out deleted documents.
'''