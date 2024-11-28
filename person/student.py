from .person import Person

class Student(Person):
    def __init__(self, name, email, phone,student_email):
        super().__init__(name, email, phone)
        self.student_email = student_email
        self.absent = False
        
        
    def mark_as_absent(self):
        self.absent = True
        
    def print_student_status(self):
        if self.absent:
            print("Student is absent")
        else:
            print("Student is present ")
    
    def __str__(self):
        
        return self.name