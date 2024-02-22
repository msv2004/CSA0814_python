import csv

def create_contact(phonebook, name, phone_number):
    phonebook[name] = phone_number

def find_phone_number(phonebook, name):
    return phonebook.get(name, "Contact not found")

def save_to_file(phonebook, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, phone_number in phonebook.items():
            writer.writerow([name, phone_number])

def main():
    
    phonebook_file_path = r"C:\SOFTWARE APPS\codes\phonebook.csv"
    phonebook = {}

    
    try:
        with open(phonebook_file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    name, phone_number = row
                    phonebook[name] = phone_number
    except FileNotFoundError:
        print(f"Phonebook file '{phonebook_file_path}' not found. Creating a new one.")

    while True:
        print("\nEnter 'C' to create a new contact, 'R' to find a phone number, 'E' to exit.")
        choice = input("Your choice: ").upper()

        if choice == 'C':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            create_contact(phonebook, name, phone_number)
            print(f"Contact '{name}' added.")

        elif choice == 'R':
            name = input("Enter the name to find the phone number: ")
            result = find_phone_number(phonebook, name)
            print(f"Phone number for '{name}': {result}")

        elif choice == 'E':
            save_to_file(phonebook, phonebook_file_path)
            print(f"Contacts saved to '{phonebook_file_path}'. Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 'C', 'R', or 'E'.")

if _name_ == "_main_":
    main()
