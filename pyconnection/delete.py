from pymongo import MongoClient
client=MongoClient("localhost:27017")
db =client.database
def delete():
    try:
        name=input("\nEnter name to delete Details\n")
        
        db.details.delete_many({"name":name})
        print("\n Data Delete Successfully")

        
      
    except Exception:
        print(str(e))
        delete()
        
