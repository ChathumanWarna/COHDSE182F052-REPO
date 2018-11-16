import pymongo
client = pymongo.MongoClient(" mongodb://127.0.0.1:27017")
db = client["Users"]
collection = db["accounts"]

Username = input("Enter UserName : ")
Password = input("Enter Password : ")
for x in collection.find( {},{"userName":1,"passWord":1}):
	Username = str(x["userName"])
	PassWord=str(x["passWord"])

if Username == userName and Password == passWord:
	print("Login Successful!!")
else:
	print("Login Failed!!")
