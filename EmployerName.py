class Employer:
    def __init__(self):
        self.Name = input("Enter your Name")
        self.Department = input("Enter your Department")
        self.Age = input("Enter your Age")
    
    def Display(self):
        print("Your data will be displayed in this format")
        print(f"Name: {self.Name}")
        print(f"Depertment: {self.Department}")
        print(f"Age: {self.Age}")

Employer1 = Employer()
Employer1.Display()

