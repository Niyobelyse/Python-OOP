class Employer:
    def __init__(self):
        self.Name = input("Enter your Name")
        self.Department = input("Enter your Department")
        self.Age = input("Enter your Age")
    
    def Display(self):
        print("Your data will be displayed in this format")
        print("{} \t {} \t {}".format(self.Name,self.Department,self.Age))

for i in range(1,3):
    employer1 = Employer()
    employer1.Display()

