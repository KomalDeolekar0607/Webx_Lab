// 1. Create and switch to the "inventory" database
use inventory

// 2. Create and insert 10 product documents into the "products" collection
db.products.insertMany([
  { ProductID: 1, ProductName: "Smartphone", Category: "Electronics", Price: 299, Stock: 50 },
  { ProductID: 2, ProductName: "Laptop", Category: "Electronics", Price: 999, Stock: 20 },
  { ProductID: 3, ProductName: "Notebook", Category: "Stationery", Price: 3, Stock: 200 },
  { ProductID: 4, ProductName: "Pen", Category: "Stationery", Price: 1, Stock: 500 },
  { ProductID: 5, ProductName: "Television", Category: "Electronics", Price: 450, Stock: 15 },
  { ProductID: 6, ProductName: "Headphones", Category: "Electronics", Price: 75, Stock: 80 },
  { ProductID: 7, ProductName: "Desk Lamp", Category: "Furniture", Price: 40, Stock: 25 },
  { ProductID: 8, ProductName: "Backpack", Category: "Accessories", Price: 60, Stock: 30 },
  { ProductID: 9, ProductName: "Tablet", Category: "Electronics", Price: 150, Stock: 35 },
  { ProductID: 10, ProductName: "Mouse", Category: "Electronics", Price: 25, Stock: 100 }
])

// 3. Display all documents
db.products.find()

// 4. Display all products in the "Electronics" category
db.products.find({ Category: "Electronics" })

// 5. Display products in ascending order of their names
db.products.find().sort({ ProductName: 1 })

// 6. Display the details of the first 5 products
db.products.find().limit(5)

// 7. Display the categories of products with a specific name
db.products.find({ ProductName: "Laptop" }, { Category: 1, _id: 0 })

// 8. Display the number of products in the "Electronics" category
db.products.countDocuments({ Category: "Electronics" })

// 9. Display all products without the "_id" field
db.products.find({}, { _id: 0 })

// 10. Display all distinct categories of products
db.products.distinct("Category")

// 11. Display products in "Electronics" category with price > 50 and < 100
db.products.find({
  Category: "Electronics",
  Price: { $gt: 50, $lt: 100 }
})

// 12. Change the price of a product (e.g., update price of "Mouse")
db.products.updateOne(
  { ProductName: "Mouse" },
  { $set: { Price: 30 } }
)

// 13. Delete a particular product (e.g., delete product with name "Backpack")
db.products.deleteOne({ ProductName: "Backpack" })

