import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase1"]
mycol = mydb["customers1"]

for x in mycol.find():
  print(x)


