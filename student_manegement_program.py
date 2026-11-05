class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name         
        self.roll_no = roll_no    
        self.marks = marks       

    def check_result(self):
        if self.marks >= 40:
            return f"{self.name} has PASSED! "
        else:
            return f"{self.name} has FAILED. "


student1 = Student(name="Rahul", roll_no=10, marks=85)
student2 = Student(name="Akash", roll_no=15, marks=32)


print(f"Name: {student1.name} | Roll No: {student1.roll_no}")
print(student1.check_result())  

print("-" * 30)

print(f"Name: {student2.name} | Roll No: {student2.roll_no}")
print(student2.check_result())  
