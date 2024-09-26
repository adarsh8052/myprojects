contacts = {}


def add_contact(name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    print(f"\nContact {name} added successfully.")


def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("\nNo contacts found.")


def update_contact(name):
    if name in contacts:
        print(f"\nUpdating contact: {name}")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully.")
    else:
        print(f"\nContact {name} not found.")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"\nContact {name} deleted successfully.")
    else:
        print(f"\nContact {name} not found.")

#
def search_contact(name):
    if name in contacts:
        print(f"\nFound contact: {name}")
        print(f"Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print(f"\nContact {name} not found.")

def contact_book():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            update_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


contact_book()