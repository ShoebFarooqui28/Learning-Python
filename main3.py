class Emp:
    language = "Rust"
    topics = 3
    
    @staticmethod
    def greet():
        print("Good Morning")
        
    def getInfo(self):
        print(f"{self.language} : {self.topics} : {self.difficulty}") #Instance Attributes
    

        
emp1 = Emp()
emp1.language = "JavaScript"
emp1.difficulty = "Mild"

emp1.getInfo() # = Employee.getInfo(emp1)
emp1.greet() # = Employee.greet(emp1)
