class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def work(self):
        print(f"{self.name} is working.")
    def show(self):
        print(f"Employee:{self.name}, salary :{self.__salary}")
        
emp1 = Employee("abcd", 3000000)
print("Employee name--> ",emp1.name)
print("Employee salary--> ",emp1._Employee__salary)
emp1.work()
emp1.show()
    
    