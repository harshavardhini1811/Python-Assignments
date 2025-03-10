class Student:
    school_name = "ABC High School"

    def _init_(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}, School: {self.school_name}")
s1 = Student("Priya", "A")
s2 = Student("Rahul", "B")
s1.display()
s2.display()