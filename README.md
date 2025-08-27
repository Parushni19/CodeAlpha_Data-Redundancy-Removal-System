# 🗂️ Data Redundancy Removal System (Task 2)

# Introduction
This project is a **Data Redundancy Removal System** built using **Python** and **MongoDB**.  
It prevents duplicate records from being stored in the database by generating a **SHA256 hash** for each entry.

# Features
✅ Insert new record (checks for duplicates before saving)  
✅ Bulk insert multiple records  
✅ View all stored records  
✅ Prevents redundancy using hashing  

---

# Technologies Used
1) Python 3  
2) MongoDB
3) PyMongo library  
4) Hashlib (for SHA256 hashing)  

# How to Run

1. Clone the repository:
   ```bash

   git clone <your-repo-link>
   cd <repo-name>

2. Install dependencies:

   pip install pymongo

4. Start MongoDB (make sure it is running on your system):

   mongod

4.Run the project:

   python main.py

-> Starting Redundancy Removal System...

Choose an option:
1. Insert new record
2. Bulk insert records
3. View all records
4. Exit
Enter choice (1/2/3/4):

-> Example when trying to insert duplicate:

Record already exists! ⚠️
