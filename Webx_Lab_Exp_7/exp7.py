from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
print("\nConnected to database")

# Create database
db = client["StudentsDB"]  # Database will be created when a collection is added
print("\nCreated the database")

# Create collection
collection = db["IT_dept"]
print("\nCreated the Collection")

student = {"Name": "Komal Deolekar", "RollNo": 131, "Class": "IT-A"}
# collection.insert_one(student)
# collection.insert_one({"Name": "Komal", "RollNo": 101, "Class": "IT-A"})
print("\nInserted one student record")

for stu in collection.find({}):
    print(stu)

students = [
    {"Name": "Amit Sharma", "RollNo": 101, "Class": "D5A"},
    {"Name": "Priya Mehta", "RollNo": 102, "Class": "D5B"},
    {"Name": "Rahul Verma", "RollNo": 103, "Class": "D5C"},
    {"Name": "Sneha Patil", "RollNo": 104, "Class": "D10A"},
    {"Name": "Rohan Kulkarni", "RollNo": 105, "Class": "D10B"},
    {"Name": "Neha Gupta", "RollNo": 106, "Class": "D10C"},
    {"Name": "Vikas Yadav", "RollNo": 107, "Class": "D15A"},
    {"Name": "Anjali Nair", "RollNo": 108, "Class": "D15B"},
    {"Name": "Arjun Singh", "RollNo": 109, "Class": "D15C"},
    {"Name": "Komal Deolekar", "RollNo": 110, "Class": "D20A"},
    {"Name": "Siddharth Desai", "RollNo": 111, "Class": "D20B"},
    {"Name": "Pooja Iyer", "RollNo": 112, "Class": "D20C"},
    {"Name": "Varun Malhotra", "RollNo": 113, "Class": "D5A"},
    {"Name": "Kiran Rao", "RollNo": 114, "Class": "D10B"},
    {"Name": "Meera Joshi", "RollNo": 115, "Class": "D15A"},
    {"Name": "Rajesh Kumar", "RollNo": 116, "Class": "D5B"},
    {"Name": "Nidhi Agarwal", "RollNo": 117, "Class": "D5C"},
    {"Name": "Akash Singh", "RollNo": 118, "Class": "D10A"},
    {"Name": "Simran Kaur", "RollNo": 119, "Class": "D10C"},
    {"Name": "Yash Raj", "RollNo": 120, "Class": "D15B"},
    {"Name": "Deepak Tiwari", "RollNo": 121, "Class": "D15C"},
    {"Name": "Harsha Reddy", "RollNo": 122, "Class": "D20A"},
    {"Name": "Vivek Chauhan", "RollNo": 123, "Class": "D20B"},
    {"Name": "Shweta Pandey", "RollNo": 124, "Class": "D20C"},
    {"Name": "Ayesha Khan", "RollNo": 125, "Class": "D5A"},
    {"Name": "Pankaj Sinha", "RollNo": 126, "Class": "D10A"},
    {"Name": "Gaurav Saxena", "RollNo": 127, "Class": "D15A"},
    {"Name": "Bhavana Menon", "RollNo": 128, "Class": "D20C"},
    {"Name": "Manoj Pillai", "RollNo": 129, "Class": "D5B"},
    {"Name": "Tanya D'Souza", "RollNo": 130, "Class": "D10B"}
]
# collection.insert_many(students)
print("\nMultiple student records inserted!")

for stu in collection.find({}):
    print(stu)

print("\nD15A Student List : ")
for product in collection.find({"Class": "D15A"}):
    print(product)

student = collection.find_one({"RollNo" : 131})
print(f"\nStudent with Roll No. 131 : ${student}")

print("\nRoll number in [101, 105, 110, 120, 130]")

# List of roll numbers to search for
roll_numbers = [101, 105, 110, 120, 130]

# Find students with these roll numbers
students = collection.find({"RollNo": {"$in": roll_numbers}})

# Print the results
for student in students:
    print(student)

print("\nwith direct List : ")

# Find students with these roll numbers
students = collection.find({"RollNo": {"$in": [101, 105, 110, 120, 130]}})

# Print the results
for student in students:
    print(student)

collection.update_one({"Name" : "Vivek Chauhan"}, {"$set":{"RollNo": 132}})
print("\nRoll number updated")

student = collection.find_one({"RollNo" : 132})
print("\nUpdated data :",student)

collection.delete_one({"Name" : "Manoj Pillai"})
print("\nManoj Pillai's record deleted")

print("\nPrinting the data..")
for stu in collection.find({}):
    print(stu)