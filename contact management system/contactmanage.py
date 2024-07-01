import json

# Global variable to store contacts
contacts = []

def save_contacts_to_file():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def load_contacts_from_file():
    global contacts
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

def add_contact():
    print("\nEnter contact details:")
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    
    contacts.append(contact)
    save_contacts_to_file()
    print(f"\nContact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("\nContact list is empty.")
    else:
        print("\n--- Contact List ---")
        for idx, contact in enumerate(contacts):
            print(f"{idx+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact():
    view_contacts()
    if contacts:
        try:
            idx = int(input("\nEnter the number of the contact you want to edit: ")) - 1
            if 0 <= idx < len(contacts):
                print(f"\nEditing contact: {contacts[idx]['name']}")
                contacts[idx]['name'] = input("New name (leave empty to keep current): ") or contacts[idx]['name']
                contacts[idx]['phone'] = input("New phone number (leave empty to keep current): ") or contacts[idx]['phone']
                contacts[idx]['email'] = input("New email address (leave empty to keep current): ") or contacts[idx]['email']
                save_contacts_to_file()
                print("\nContact updated successfully!")
            else:
                print("\nInvalid contact number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid contact number.")

def delete_contact():
    view_contacts()
    if contacts:
        try:
            idx = int(input("\nEnter the number of the contact you want to delete: ")) - 1
            if 0 <= idx < len(contacts):
                print(f"\nDeleting contact: {contacts[idx]['name']}")
                del contacts[idx]
                save_contacts_to_file()
                print("Contact deleted successfully!")
            else:
                print("\nInvalid contact number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid contact number.")

def main():
    load_contacts_from_file()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit a Contact")
        print("4. Delete a Contact")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("\nExiting the program... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
