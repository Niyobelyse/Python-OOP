class Telephone:
    """ This allow calling if the name is in directory"""
    def __init__(self):
        self.phonenumber = int(input("Please register phone number"))
        self.name = input("Please register it's name")
        self.Phonebook = {self.phonenumber: self.name}
    

    def Calling(self):
        self.name_to_call = input("Enter name to call")
        if self.name_to_call in self.Phonebook.values():
            print(f"Calling {self.name_to_call}")
        else:
            print(f"We don't have {self.name_to_call} in phonebook")



class CellPhone(Telephone):
    def __init__(self):
        super().__init__()
    def Messaging(self):
        self.name_to_message = input("Enter name to massage")
        if self.name_to_message in self.Phonebook.values():
            print(f"Message to {self.name_to_message}")
        else:
            print(f"We don't have {self.name_to_message} in phonebook")      


phone1=CellPhone()
phone1.Calling()
phone1.Messaging()