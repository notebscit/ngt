from pymongo import MongoClient
client=MongoClient("localhost:27017")
db =client.database
def update():
    try:
        name=input("\nEnter name to update Details\n")
        age=input("\nEnter age\n")
        rollno=input("\nEnter Roll no.\n")
        country=input("\nEntercountry\n")
        db.details.update_one({"name":name},
                              {
                                  "$set":{
                                      "age":age,
                                      "rollno":rollno,
                                      "country":country

                                      }})
        print("\n Data Update Successfully")

        
      
    except Exception:
        print(str(e))
        update()
        
