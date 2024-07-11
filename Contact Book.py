# Contact Design
'''
contact = [
    {
        "f_name": "Mahmud",
        "l_name": "Faisal",
        "email": "pepsi.shuva@gmail.com",
        "phone_number": "+55 555-5555",
        "DoB": "05/09/1984"
    },
    {
        "f_name": "Mahmud",
        "l_name": "Faisal",
        "email": "pepsi.shuva@gmail.com",
        "phone_number": "+55 555-5555",
        "DoB": "05/09/1984"
    },
]
'''
contact_list = []


def create_contact():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    DoB = input("Enter your date of birth: ")
    contact = {
        "first name": f_name,
        "last name": l_name,
        "email": email,
        "phone number": phone_number,
        "Date of Birth": DoB
    }
    contact_list.append(contact)
    print("Contact has been created successfully!")
    return contact_list


create_contact()


def view_all_contacts():
    for i in contact_list:
        print(f"First Name: {i['first name']}",
              f"Last Name: {i['last name']}",
              f"Email: {i['email']}",
              f"Phone Number: {i['phone number']}",
              f"Date of Birth: {i['Date of Birth']}",
              sep=", ")
        print("\n")
        # print("-"*50)
        # print("\n")


view_all_contacts()


def search_contact():
    search = input("Enter your search term: ")
    for i in contact_list:
        if search.lower() in i["First Name"].lower():
            print(f"Found!\n"
                  f"First Name: {i['First name']}",
                  f"Last Name: {i['last name']}",
                  f"Email: {i['email']}",
                  f"Phone Number: {i['phone number']}",
                  f"Date of Birth: {i['Date of Birth']}",
                  sep=", ")


search_contact()


def delete_contact():
    search = input("Enter your search term to delete: ")
    for index, contact in enumerate(contact_list):
        if search.lower() in contact["First Name"].lower():
            print(f"Found!\n"
                  f"{index+1}. {contact['First name']} = {contact['phone number']}",)
    selected = int(input("Enter index to delete: "))
    contact_list.pop(selected - 1)
    print("Contact has been deleted successfully!")


delete_contact()
view_all_contacts()
