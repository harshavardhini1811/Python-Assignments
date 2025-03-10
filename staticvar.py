class Student:
    school_name = " Girls   High School"

    def _init_(self, name, grade):
        self.name = name
        self.grade = grade
print("Accessing through class:", Student.school_name)
s1 = Student("Priya", "A")
s2 = Student("Rahul", "B")
print("Accessing through instance:", s1.school_name)
print("Accessing through instance:", s2.school_name)
Student.school_name = "Public International School"

print("\nAfter modifying through class name:")
print("Accessing through class:", Student.school_name)
print("Accessing through instance:", s1.school_name)
print("Accessing through instance:",s2.school_name)

