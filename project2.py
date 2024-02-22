import csv

class Phonebook:
    def __init__(self):
        self.contacts = {}

    def create_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Contact '{name}' added successfully.")

    def find_phone_number(self, name):
        return self.contacts.get(name, "Name not found")

    def save_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for name, phone_number in self.contacts.items():
                writer.writerow([name, phone_number])

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        name, phone_number = row
                        self.contacts[name] = phone_number
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    def get_all_contacts(self):
        return self.contacts

def main():
    phonebook = Phonebook()
    phonebook.load_from_file("phonebook.csv")

    try:
        while True:
            print("Enter 'C' to create a new contact, 'R' to find out the phone number of a person, 'E' to exit and save:")
            choice = input().upper()

            if choice == 'C':
                name = input("Enter the name: ")
                phone_number = input("Enter the phone number: ")
                phonebook.create_contact(name, phone_number)

            elif choice == 'R':
                name = input("Enter the name to find the phone number: ")
                phone_number = phonebook.find_phone_number(name)
                print(f"Phone number for '{name}': {phone_number}")

            elif choice == 'E':
                phonebook.save_to_file("phonebook.csv")
                print("Phonebook saved successfully. Exiting.")
                break

            else:
                print("Invalid choice. Please enter 'C', 'R', or 'E'.")

    except Exception as e:
        print(f"Error: {e}")

    return phonebook.get_all_contacts()

if __name__ == "__main__":
    all_contacts = main()
    print("All Contacts:", all_contacts)
