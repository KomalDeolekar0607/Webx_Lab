// Base class Student
class Student {
    constructor(public name: string, public studentId: number, public grade: string) {}

    getDetails(): string {
        return `Student Name: ${this.name}, ID: ${this.studentId}, Grade: ${this.grade}`;
    }
}

// Subclass GraduateStudent
class GraduateStudent extends Student {
    constructor(name: string, studentId: number, grade: string, public thesisTopic: string) {
        super(name, studentId, grade);
    }

    getThesisTopic(): string {
        return `Thesis Topic: ${this.thesisTopic}`;
    }

    getDetails(): string {
        return `Graduate Student Name: ${this.name}, ID: ${this.studentId}, Grade: ${this.grade}, Thesis: ${this.thesisTopic}`;
    }
}

// Independent class LibraryAccount (Composition over Inheritance)
class LibraryAccount {
    constructor(public accountId: number, public booksIssued: number) {}

    getLibraryInfo(): string {
        return `Library Account ID: ${this.accountId}, Books Issued: ${this.booksIssued}`;
    }
}

// Creating instances
const student = new Student("Alice", 101, "A");
console.log(student.getDetails());

const gradStudent = new GraduateStudent("Bob", 102, "A+", "Machine Learning");
console.log(gradStudent.getDetails());
console.log(gradStudent.getThesisTopic());

const libraryAccount = new LibraryAccount(2001, 5);
console.log(libraryAccount.getLibraryInfo());

// Associating LibraryAccount with Student
const studentLibraryMapping = { student, libraryAccount };
console.log(studentLibraryMapping.student.getDetails());
console.log(studentLibraryMapping.libraryAccount.getLibraryInfo());
