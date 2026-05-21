class Contact:
    def __init__(self):
        self.contacts = {}
    def addcontact(self):
        name = input("Enter name: ")
        mobile = input("Enter mobile no: ")
        mailid = input("Enter mailid: ")
        self.contacts[name] = {
            "mobile": mobile,
            "mailid": mailid}
        print("Contact Added Successfully")
    def update(self):
        name = input("Enter contact name to update: ")
        if name in self.contacts:
            field = input("What do you want to update? mobile/mailid: ").lower()
            new_value = input(f"Enter new {field}: ")
            self.contacts[name][field] = new_value
            print("Updated Successfully")
        else:
            print("Contact not found")
    def listcontact(self):
        if len(self.contacts) == 0:
            print("No contacts available")
        else:
            print("\n{:<15} {:<15} {:<25}".format("NAME", "MOBILE", "MAIL ID"))
            print("-" * 55)
            for name, details in self.contacts.items():
                mobile = details.get("mobile", "Not Available")
                mailid = details.get("mailid", "Not Available")
                print("{:<15} {:<15} {:<25}".format(name, mobile, mailid))
    def remove(self):
        name = input("Enter contact name: ")
        if name in self.contacts:
            field = input("What do you want to delete? mobile/mailid: ").lower()
            if field in self.contacts[name]:
                del self.contacts[name][field]
                print("Deleted Successfully")
                print(self.contacts)
            else:
                print("Field not found")
        else:
            print("Contact not found")

x = Contact()
while True:
    option = int(input("""
1) Add Contact
2) Update Contact
3) List Contact
4) Remove Contact
5) Exit"""))

    if option == 1:
        x.addcontact()
    elif option == 2:
        x.update()
    elif option == 3:
        x.listcontact()
    elif option == 4:
        x.remove()
    elif option == 5:
        break
    else:
        print("Invalid Choice")
