import csv

contacts_file = 'task5.csv'

def load_contacts():
    contacts = []
    try:
        with open(contacts_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        with open(contacts_file, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email', 'address'])
            writer.writeheader()
    return contacts

def save_contacts(contacts):
    with open(contacts_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email', 'address'])
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(name, phone, email, address):
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)

def view_contacts():
    if not contacts:
        print("No contacts found.")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(query):
    found_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact['phone'] = phone
            contact['email'] = email
            contact['address'] = address
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    save_contacts(contacts)
    print("Contact deleted.")

def main():
    global contacts
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            update_contact(name)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
