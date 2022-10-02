from pymongo import MongoClient
client=MongoClient("localhost:27017")
db=client.krish
def insert():
    try:
        eid=input("Enter the ID of student ")
        ename=input("Enter the nam of Studnet ")
        eage=input("Enter age of student ")
        ecountry=input("Enter Country of student ")

        db.details.insert_one({
            "eid":eid,
            "ename":ename,
            "eage":eage,
            "ecountry":ecountry
            })
        print("\n Data Insered successfully!!\n")
    except Exception:
        print(str(e))
        insert()


        
