class Student:
    def __init__(self, name, current_class, id) -> None:
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str:
        return f"Student with name: {self.name}, class: {self.current_class}, id: {self.id}"

class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f"Teacher: {self.name}, subject: {self.subject}"

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return "Not enough Fee"
        else:
            id = len(self.students) + 1  # Corrected the ID generation for students
            student = Student(name, "current_class", id)
            self.students.append(student)
            return f"{name} is enrolled with id: {id}, extra money: {fee - 6500}"

    def __repr__(self) -> str:
        result = f"Welcome to {self.name}\n"
        result += "____Our Teachers____\n"
        for teacher in self.teachers:
            result += str(teacher) + "\n"
        result += "____Our Students____\n"
        for student in self.students:
            result += str(student) + "\n"
        return result

# Testing the classes
ripa = Student("ripa", 10, 1)
print(ripa)

Binoy = Teacher("Binoy sir", "Bangla", 101)
print(Binoy)

cse = School("CSE")
print(cse.enroll("ripa", 5200))  # Not enough fee
print(cse.enroll("ripa", 6500))  # Successful enrollment
cse.add_teacher("Binoy sir", "Algo")

print(cse)
