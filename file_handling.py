# "name", "address", "age", "grade"
import csv

class Student:
    def __init__ (self, name, address, age, grade):
        self.name = name
        self.address = address
        self.age = int(age)
        self.grade = grade

    def values(self):
        return [self.name, self.address, self.age, self.grade]

students = []
# EXTRACT
with open("students.csv") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace = True)

    next(reader)

    for row in reader:
        current_student = Student(*row)
        students.append(current_student)

# TRANSFORM
for student in students:
    student.age += 1
    if student.name == "Samantha Barrett":
        student.address = "4B Canyon Road"
    if student.grade == "B+":
        student.grade = "A-"


# WRITE
with open("students_write.csv", mode = "w") as csvfile:
    writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
    writer.writerow(["name", "address", "age", "grade"])

    for student in students:
        writer.writerow(student.values())
