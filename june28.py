class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("I am a person and my name is " + self.name)

p1 = Person ("John", 36)
p1.myfunc()

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def namefunc(self):
        print("I am a student and my name is " + self.name)

    def agefunc(self):
        print("I am a student and my age is " + str(self.age))

    def gpafunc(self):
        print("I am a student and my gpa is " + str(self.gpa))

s1 = Student("David", 15, 4.0)
s1.namefunc()
s1.agefunc()
s1.gpafunc()

class Course:
    def __init__(self, name, listofstuds):
        self.name = name
        self.listofstuds = listofstuds

    def namefunc(self):
        print("The course's name is " + self.name)

    def thelist(self):
        print("List of studdents in this course are " + ", ".join(self.listofstuds))

c1 = Course("Artifical Intelligence", ['Alice', 'Ben', 'Cathy' ,'David', 'Eli'])
c1.namefunc()
c1.thelist()
