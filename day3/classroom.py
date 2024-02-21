class Person():
    firstname = "unknown"
    lastname = "unknown"

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def person_info(self):
        print(f"First name: {self.firstname}, Last name: {self.lastname}")

# To confirm that it works:
d = Person("Tim","Eriksson")
d.person_info()

class Student(Person):
    subject = "unkown"

    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        print(f"{self.firstname} {self.lastname} has subject {self.subject}")

# To confirm that it works
s = Student("Lara", "Langstrump", "Chemistry")
s.printNameSubject()


class Teacher(Person):
    course = "unkown"

    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course 

    def printNameCourse(self):
        print(f"{self.firstname} {self.lastname} has teaches {self.course}")

