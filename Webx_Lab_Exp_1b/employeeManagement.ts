interface Employee {
    name: string;
    id: number;
    role: string;
    getDetails(): string;
}

// Manager class implementing Employee interface
class Manager implements Employee {
    constructor(public name: string, public id: number, public role: string, public department: string) {}

    getDetails(): string {
        return `Manager Name: ${this.name}, ID: ${this.id}, Role: ${this.role}, Department: ${this.department}`;
    }
}

// Developer class implementing Employee interface
class Developer implements Employee {
    constructor(public name: string, public id: number, public role: string, public programmingLanguages: string[]) {}

    getDetails(): string {
        return `Developer Name: ${this.name}, ID: ${this.id}, Role: ${this.role}, Languages: ${this.programmingLanguages.join(", ")}`;
    }
}

// Creating instances
const manager = new Manager("Charlie", 201, "Manager", "Software Development");
console.log(manager.getDetails());

const developer = new Developer("David", 202, "Developer", ["TypeScript", "JavaScript", "Python"]);
console.log(developer.getDetails());
