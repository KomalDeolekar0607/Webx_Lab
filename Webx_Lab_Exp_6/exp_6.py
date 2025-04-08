from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update if using a different host or port
print("Connected to MongoDb")

db = client["inventory"]  # Create or connect to the 'inventory' database
print("Created Inventory DataBase")

collection = db["products"]  # Create or connect to the 'products' collection
print("Created Products collection")

# Insert 10 documents
products = [
    {"ProductID": 1, "ProductName": "Laptop", "Category": "Electronics", "Price": 800, "Stock": 10},
    {"ProductID": 2, "ProductName": "Smartphone", "Category": "Electronics", "Price": 500, "Stock": 25},
    {"ProductID": 3, "ProductName": "Headphones", "Category": "Electronics", "Price": 50, "Stock": 50},
    {"ProductID": 4, "ProductName": "Table", "Category": "Furniture", "Price": 150, "Stock": 15},
    {"ProductID": 5, "ProductName": "Chair", "Category": "Furniture", "Price": 80, "Stock": 30},
    {"ProductID": 6, "ProductName": "T-shirt", "Category": "Clothing", "Price": 20, "Stock": 100},
    {"ProductID": 7, "ProductName": "Shoes", "Category": "Clothing", "Price": 60, "Stock": 40},
    {"ProductID": 8, "ProductName": "TV", "Category": "Electronics", "Price": 900, "Stock": 5},
    {"ProductID": 9, "ProductName": "Watch", "Category": "Accessories", "Price": 120, "Stock": 20},
    {"ProductID": 10, "ProductName": "Bag", "Category": "Accessories", "Price": 40, "Stock": 35},
    {"ProductID": 11, "ProductName": "Laptop", "Category": "Electronics", "Price": 1000, "Stock": 15},
    {"ProductID": 12, "ProductName": "Jeans", "Category": "Clothing", "Price": 500, "Stock": 12},
     {"ProductID": 13, "ProductName": "Lesor", "Category": "Electronics", "Price": 90, "Stock": 15},
      {"ProductID": 14, "ProductName": "Jacket", "Category": "Clothing", "Price": 400, "Stock": 12},
       {"ProductID": 15, "ProductName": "Bulb", "Category": "Electronics", "Price": 70, "Stock": 25},
]

# Insert data into MongoDB
collection.insert_many(products)
print("\n Inserted 10 products successfully.")

# Display all documents
print("\n All Products:")
for product in collection.find():
    print(product)

# Display all products in 'Electronics' category
print("\n Electronics Products:")
for product in collection.find({"Category": "Electronics"}):
    print(product)

# Display all products in ascending order of ProductName
print("\n Products Sorted by Name:")
for product in collection.find().sort("ProductName",1):
    print(product)


# Display categories of products with a specific name
product_name = "Laptop"
print(f"\n Category of '{product_name}':")
for product in collection.find({"ProductName":product_name}):
    print(product)

# Display categories of products with a specific name
product_name = "Laptop"
print(f"\n Category of '{product_name}':")
for product in collection.find({"ProductName":product_name},{ "ProductName" : 1 ,"Category":1,"_id" : 0}):
    print(product)


# Display the number of products in the 'Electronics' category
electronics_count = collection.count_documents({"Category":"Electronics"})
print(f"\n Number of Electronics Products: {electronics_count}")

# Display all products without the "_id" field
print("\n Products Without '_id':")
for product in collection.find({},{"_id":0}):
    print(product)

# Display all distinct categories
# for category in collection.distinct("Category"):
#     print(category)

# Display all distinct categories
categories = collection.distinct("Category")
print("\n Distinct Product Categories:", categories)

# Display products in 'Electronics' category with prices >50 and <100
print("\n Electronics Products with Price Between 50 and 100:")
for product in collection.find({"Category":"Electronics" , "Price" : {"$gt" : 50 , "$lt" : 100 }}):
    print(product)

# Update the price of a product
collection.update_one({'ProductName': 'TV'}, {"$set" : {"Price" : 850}})
print("\n Price of Laptop updated to 850.")

product = collection.find_one({"ProductName" : "TV"})
print(product)

# Delete a particular product entry
collection.delete_one({"ProductName" : "Chair"})
print("\n Product 'Chair' deleted.")

for product in collection.find({"ProductName" : "Chair"}):
    print(product)



