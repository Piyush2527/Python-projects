class phonebook:
    phone_dicrectory = [] 

    def __init__(self,name,p_number):
        self.name = name
        self.p_number = p_number
        # phonebook.phone_dicrectory[self.name] = self.p_number # using dictionary
        phonebook.phone_dicrectory.append(self) # using list of objects

    def show_contacts(self):
        return f"Name: {self.name}, Phone Number: {self.p_number}"
    
    @classmethod
    def search_contact(cls, name):
        for contact in cls.phone_dicrectory:
            if contact.name.lower() == name.lower():
                return contact.show_contacts()
        return "Contact not found."
    
    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_dicrectory)==0:
            print("Phonebook is empty.")
        else:
            for contact in cls.phone_dicrectory:
                print(contact.show_contacts())

    @staticmethod
    def help():
        return "This is a simple phonebook application to store and retrieve contacts."
    def validate_number(p_number):
        # simple validation: check if the number contains only digits and has 10 characters
        if p_number.isdigit() and len(p_number) == 10:
            return True
        return False
    
# displaying help information
print()
print(phonebook.help())
print()

# creating objects
n_ops = int(input("Enter number of contacts to add: "))
while n_ops>0:
    name = input("Enter name: ")
    p_number = input("Enter phone number: ")
    if phonebook.validate_number(p_number):
        contact = phonebook(name, p_number)
        print(f"Contact '{name}' added successfully.")
        n_ops -= 1
    else:
        print("Invalid phone number. Please enter a 10-digit number.")
    print()

# showing all contacts using class method
print("All Contacts in Phonebook:")
phonebook.show_all_contacts()
print()

# searching for a contact
search_name = input("Enter the name to search for: ")
print(f"Searching for contact '{search_name}':")
print(phonebook.search_contact(search_name))


