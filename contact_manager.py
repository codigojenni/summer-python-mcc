import csv

FILENAME = "contacts.csv"

def create_csv_file():
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
    print("\nContact file created successfully!\n")


def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print("Contact added successfully!\n")


def view_contacts():
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    except FileNotFoundError:
        print("\nNo contact file found. Please create it first.\n")
        return

    if len(contacts) <= 1:
        print("\nNo contacts found.\n")
    else:
        print("\nContacts Information:")
        print("----------------------------")
        print("Name, Phone, Email")
        print("----------------------------")
        for contact in contacts[1:]:
            name = contact[0].strip()
            phone = contact[1].strip()
            email = contact[2].strip()
            print(f"{name}, {phone}, {email}")
        print()


def edit_contact():
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    except FileNotFoundError:
        print("\nNo contact file found. Please create it first.\n")
        return

    if len(contacts) <= 1:
        print("\nNo contacts available to edit.\n")
        return

    print("\nCurrent Contacts:")
    print("----------------------------")
    print("Name, Phone, Email")
    print("----------------------------")
    for contact in contacts[1:]:
        print(f"{contact[0]}, {contact[1]}, {contact[2]}")
    print()

    name_to_edit = input("Enter the name of the contact you want to edit: ")
    index_to_edit = -1

    for i in range(1, len(contacts)):
        if contacts[i][0].strip().lower() == name_to_edit.strip().lower():
            index_to_edit = i
            break

    if index_to_edit == -1:
        print("Contact not found.\n")
        return

    current = contacts[index_to_edit]
    print(f"\nCurrent details - Name: {current[0]}, Phone: {current[1]}, Email: {current[2]}")

    new_phone = input("Enter new phone number (leave blank to keep current): ")
    new_email = input("Enter new email address (leave blank to keep current): ")

    if new_phone != "":
        contacts[index_to_edit][1] = new_phone
    if new_email != "":
        contacts[index_to_edit][2] = new_email

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

    print("Contact updated successfully!\n")


def display_menu():
    print("Contact Manager App")
    print("----------------------------")
    print("1 - Create a new contact file")
    print("2 - Add a new contact")
    print("3 - View all contacts")
    print("4 - Modify an existing contact")
    print("5 - Exit the program")
    print()


def main():
    print("Welcome! This program helps you manage your contact list using a CSV file.\n")

    while True:
        display_menu()
        choice = input("Enter your selection: ")

        if choice == "1":
            create_csv_file()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            print("\nCompleted by, Jennifer Mendoza Trejo")
            break
        else:
            print("\nInvalid option. Please try again.\n")


main()
