'''2. create a python class called birthdayboy that takes 2 variables:
     a. A string name
     b. An integer age
     within the class . create a method called birthday that increases the value of age by 1. create an instances of the class then call birthday methods on that to increase its age and print he same.''' 
class birthdayboy:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def birthday(self):
        self.age+=1 
        print(self.age)
        
        
x1 = birthdayboy('John', 23)
x1.birthday()

