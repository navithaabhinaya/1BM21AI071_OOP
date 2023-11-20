'''write a python program to create two empty classes, Student and Marks. Now create some instance and check whether they are instances of said classes or not. Also, check whether the said classes are subclasses of the built-in objects or not.''' 
class Student:
    pass
class Marks:
    pass
student1=Student()
mark1 = Marks()
student2 = Student()
mark44 = Marks()
print(isinstance(student1, Student))
print(isinstance(student2, Student))
print(isinstance(mark1, Marks))
print(isinstance(mark44, Marks))


