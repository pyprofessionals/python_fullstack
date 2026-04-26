#Student Mark Management
#(class,def,object,constructors)
#(Five Subject Get, Total , Average, result, cell function)

class Student:
    #constructor
    def __init__(self,name,mark1,mark2,mark3,mark4,mark5):
        self.name = name
        self.std = "X"
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        self.mark5 = mark5
    def total(self):
        return self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5 
    def average(self):
        return self.total() // 5
    def result(self):
        return self.average()<=45
    def show(self):
        print("Student Name:",self.name)
        print("Std:",self.std)
        print("Total Marks:",self.total())
        print("Average Mark Of Student:",self.average())
        print("The Student Is Pass",self.result())
while True:
    name=input("Enter A Student Name:")
    mark1=int(input("Enter Marks1:"))
    mark2=int(input("Enter Marks2:"))
    mark3=int(input("Enter Marks3:"))
    mark4=int(input("Enter Marks4:"))
    mark5=int(input("Enter Marks5:"))

    Student1 = Student(name,mark1,mark2,mark3,mark4,mark5)
    Student1.show()

    choice = input("Is You Want Continue(1/0)")
    if choice==0:
        break
