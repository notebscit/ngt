from pymongo import MongoClient
client=MongoClient("localhost:27017")
db =client.database
def read():
    try:
        sdetials=db.details.find({},{"_id":0})
        
        print("\n all the data from database!!!\n")
        for det in sdetials:
            print(det)
            
    except Exception:
        print(str(e))
        read()
        
