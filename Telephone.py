class Telephone:
    """ This allow calling if the name is in directory"""
    def __init__(self):
        self.phonenumber = int(input("Please register phone number"))
        self.name = input("Please register it's name")
        self.Phonebook = {self.phonenumber: self.name}
    

    def Calling(self):
        if self.name in self.Phonebook.values():
            print(f"Calling {self.name}")
        else:
            print("We don't have {self.name} in phonebook")



phone1 = Telephone()
phone1.Calling()
  