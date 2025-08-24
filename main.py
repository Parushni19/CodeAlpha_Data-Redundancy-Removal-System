from pymongo import MongoClient
import hashlib

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["redundancy_db"]
collection = db["records"]

def get_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def insert_record(data: str):
    record_hash = get_hash(data)
    existing = collection.find_one({"hash": record_hash})
    if existing:
        print(f"⚠️ Duplicate skipped: {data}")
    else:
        collection.insert_one({"data": data, "hash": record_hash})
        print(f"✅ Inserted: {data}")

def view_records():
    print("\n📂 Records in database:")
    for record in collection.find():
        print(f"- {record['data']} (hash: {record['hash'][:10]}...)")
    print()

def bulk_insert():
    print("\n✍️ Enter multiple records (type 'done' to finish):")
    while True:
        data = input("Record: ").strip()
        if data.lower() == "done":
            break
        if data:
            insert_record(data)

def main():
    print("🚀 Data Redundancy Removal System Started 🚀")
    while True:
        print("\nChoose an option:")
        print("1. Insert new record")
        print("2. Bulk insert records")
        print("3. View all records")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ").strip()
        
        if choice == "1":
            data = input("Enter your record: ").strip()
            insert_record(data)
        elif choice == "2":
            bulk_insert()
        elif choice == "3":
            view_records()
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
