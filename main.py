import pymongo

#Provide the mongodb localhost url to connect pythonto mongodb
client=pymongo.MongoClient("mongodb://localhost:27017/nuerolabDB")

#Database Name
database=client["nuerolabDB"]

#Collection Name
collection=database["Products"]

#Sample data
d={'companyName':'NavinFlourine',
'product':'Affordable AI',
'courseOffered':'Machine Learning with Deployment'}

#Insert above records in the collection
rec=collection.insert_one(d)

#Let's verify all the record at once present in the record with all the fields
all_record=collection.find()

#Printing all records present in the collection
for idx, record in enumerate(all_record):
    print(f"{idx}:{record}")