type StudentInfo = {
    id : number,
    name : String , 
    surname : String,
    marks : number , 
    age : number
}

const studentsInfo : StudentInfo[] = [
{ id: 1, name: "Alice", age: 20, marks: 85 ,surname : "Johnson"},
  { id: 2, name: "Bob", age: 21, marks: 72 , surname:"Smith" },
  { id: 3, name: "Charlie", age: 19, marks: 55 , surname: "Brown"},
  { id: 4, name: "Diana", age: 22, marks: 38 , surname:"Williams"},
  { id: 5, name: "Eve", age: 20, marks: 60, surname:"Davis" },
  { id: 5, name: "Eve", surname: "Davis", age: 20, marks: 60 },
  { id: 6, name: "Frank", surname: "Taylor", age: 21, marks: 47 },
  { id: 7, name: "Grace", surname: "Wilson", age: 18, marks: 78 },
  { id: 8, name: "Hannah", surname: "Moore", age: 23, marks: 91 },
  { id: 9, name: "Ivan", surname: "Thomas", age: 20, marks: 66 },
  { id: 10, name: "Jack", surname: "Martin", age: 19, marks: 33 },
]

studentsInfo.forEach((student) =>{
    var result :String = "";
    if(student.marks < 40){
        result = "Fail";
    }
    else if(student.marks < 60){
        result = "Pass"
    }
    else if(student.marks < 75){
        result = "First Class"
    }
    else{
        result = "Distinction"
    }

    console.log(`Roll No. : ${student.id} 
    Name : ${student.name} ${student.surname}
    Age : ${student.age} 
    Result : ${result}`)

    console.log("===============================================")
})