class Empolyee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Empolyee.empCount +=1
    
    def displayCount(self):
        print ("Total employee %d") 

    def displayEmployee(self):
        print ("Name :", self.name, ", salary:", self.salary)

emp1 = Empolyee("Robot", 2000)
emp2 = Empolyee("Lucy", 3000)

emp1.displayEmployee()
emp2.displayEmployee()
