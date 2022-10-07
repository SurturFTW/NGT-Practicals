from pymongo import *

#create connection between mongodb and python
client = MongoClient('localhost',27017)

#create database
dataBase = client['demoDatabase']
print("Databse created...")

#create collection
collection = dataBase['demoCollection']
print("Collection created...")

#create docs
doc1 = [{"name": "Labdya", "age": "19", "city": "Dombivli"},{"name": "Haggu", "age": "20", "city": "Dombivli"}]

#insert docs
collection.insert_many(doc1)
print("Data inserted and stored...")

#print collection data
for i in collection.find():
    print(i)
