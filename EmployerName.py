class Employer:
    def __init__(self):
        self.Name = input("Enter your Name")
        self.Department = input("Enter your Department")
        self.Age = input("Enter your Age")
    
    def Display(self):
        print("Your data will be displayed in this format")
        print(self.Name)
        print(self.Department)
        print(self.Age)