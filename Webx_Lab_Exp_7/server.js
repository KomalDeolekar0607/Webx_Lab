const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());

// Connect to MongoDB
mongoose
  .connect("mongodb://127.0.0.1:27017/student_db")
  .then(() => console.log("Database Connected..."))
  .catch((err) => console.error("Database Connection Error:", err));

// Define Schema & Model
const StudentSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
  grade: { type: String, required: true },
});

const Student = mongoose.model("Student", StudentSchema);

// Get all students
app.get("/students", async (req, res) => {
  try {
    const students = await Student.find();
    res.status(200).json(students);
  } catch (err) {
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// Get student by ID
app.get("/students/:id", async (req, res) => {
  try {
    const student = await Student.findById(req.params.id);
    if (!student) return res.status(404).json({ error: "Student not found" });
    res.status(200).json(student);
  } catch (err) {
    res.status(500).json({ error: "Invalid Student ID" });
  }
});

// Add a new student
// app.post("/students", async (req, res) => {
//   try {
//     const newStudent = new Student(req.body);
//     await newStudent.save();
//     res.status(201).json({ message: "Student added successfully", newStudent });
//   } catch (err) {
//     res.status(400).json({ error: "Invalid data format" });
//   }
// });

app.post("/students", async (req, res) => {
    try {
      const { name, age, grade } = req.body;
  
      // Custom validation
      if (!name || !age || !grade) {
        return res.status(400).json({ error: "All fields (name, age, grade) are required" });
      }
  
      const newStudent = new Student({ name, age, grade });
      await newStudent.save();
      
      res.status(201).json({ message: "Student added successfully", student: newStudent });
    } catch (err) {
      res.status(400).json({ error: "Invalid data format" });
    }
});

// Update student details by ID
app.put("/students/:id", async (req, res) => {
  try {
    const student = await Student.findByIdAndUpdate(req.params.id, req.body, {
      new: true, // ✅ Returns updated document
      runValidators: true, // ✅ Ensures updates follow schema rules
    });

    if (!student) return res.status(404).json({ error: "Student not found" });
    res.status(200).json({ message: "Student updated successfully", student });
  } catch (err) {
    res.status(500).json({ error: "Invalid Student ID" });
  }
});

// Delete a student by ID
app.delete("/students/:id", async (req, res) => {
  try {
    const student = await Student.findByIdAndDelete(req.params.id);
    if (!student) return res.status(404).json({ error: "Student not found" });
    res.status(200).json({ message: "Student deleted successfully" });
  } catch (err) {
    res.status(500).json({ error: "Invalid Student ID" });
  }
});

// Start server
const PORT = 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port: ${PORT}`));



// const express = require("express");
// const mongoose = require("mongoose");

// const app = express()
// app.use(express.json())

// //connect to MongoDB
// mongoose.connect("mongodb://127.0.0.1:27017/student_db")
//     .then(()=> console.log("Database Conected..."))
//     .catch(err=>console.log(err))

// //define schema model
// const StudentSchema = new mongoose.Schema({
//     name : {type :String , required : true},
//     age : { type: Number, required :true},
//     grade : { type : String, required :true}
// })

// const Student = mongoose.model("Student" , StudentSchema)

// //get all students
// app.get("/students",async(req , res)=>{
//     const students = await Student.find()
//     res.json(students);
// })

// //get student by id
// app.get("/students/:id", async(req,res)=>{
//     const student = await Student.findById(req.params.id)
//     if(!student) return res.status(404).send("Student not found..")
//     res.json(student)
// })

// //add a new student
// app.post("/students", async(req , res)=>{
//     const newStudent = new Student(req.body)
//     await newStudent.save()
//     res.send("Student added successfully..")
// })

// //update student details by id 
// app.put("/students/:id" , async(req , res)=>{
//     const student = await Student.findByIdAndUpdate(req.params.id , req.body , {new : true}); //new : true will return updated document else it will return old document
//     if(!student) return res.status(404).send("Student not Found")
//     res.send("Student updated successfully")
// })

// //delete a student by id
// app.delete("/students/:id" , async(req , res)=>{
//     const student = await Student.findByIdAndDelete(req.params.id)
//     if(!student) return res.status(404).send("Student not Found")
//     res.send("Student deleted successfully..")
// })

// //start server
// const PORT = 5000;
// app.listen(PORT , ()=> console.log(`Server running on port: ${PORT}`));


