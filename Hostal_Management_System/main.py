class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id, room_number):
        super().__init__(name, age)
        self.student_id = student_id
        self.room_number = room_number

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}, Room Number: {self.room_number}"

class Hostel:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise Exception("Student with this ID already exists.")
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        if student_id not in self.students:
            raise Exception("Student not found.")
        del self.students[student_id]

    def get_student(self, student_id):
        if student_id not in self.students:
            raise Exception("Student not found.")
        return self.students[student_id]

    def list_students(self):
        return [str(student) for student in self.students.values()]

# Example usage
if __name__ == "__main__":
    hostel = Hostel()

    # Adding students
    try:
        student1 = Student("Alice", 20, "S1001", 101)
        hostel.add_student(student1)

        student2 = Student("Bob", 22, "S1002", 102)
        hostel.add_student(student2)

        # Adding a student with duplicate ID
        student_duplicate = Student("Charlie", 21, "S1001", 103)
        hostel.add_student(student_duplicate)
    except Exception as e:
        print(f"Error: {e}")

    # Listing students
    try:
        print("List of students:")
        for student_info in hostel.list_students():
            print(student_info)
    except Exception as e:
        print(f"Error: {e}")

    # Removing a student
    try:
        hostel.remove_student("S1001")
    except Exception as e:
        print(f"Error: {e}")

    # Trying to remove a non-existent student
    try:
        hostel.remove_student("S9999")
    except Exception as e:
        print(f"Error: {e}")

    # Listing students after removal
    try:
        print("List of students after removal:")
        for student_info in hostel.list_students():
            print(student_info)
    except Exception as e:
        print(f"Error: {e}")
