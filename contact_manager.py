"""
Robust Contact Manager

A command-line application for adding, finding, and deleting contacts.
Expected errors are handled with specific exception types.
"""

contacts = {}


class DuplicateContactError(Exception):
    """Raised when a contact name already exists in the contact list."""


def add_contact(name, phone):
    """Add a contact, raising DuplicateContactError for duplicate names."""
    if name in contacts:
        raise DuplicateContactError(f"{name} already exists in contacts.")
    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Display and return a contact's phone number, or return None if missing."""
    try:
        phone = contacts[name]
    except KeyError:
        print("Contact not found.")
        return None

    print(f"{name}: {phone}")
    return phone


def delete_contact(name):
    """Delete a contact, or display a message if the contact is missing."""
    try:
        del contacts[name]
    except KeyError:
        print("Contact not found.")
        return False

    print(f"Deleted {name}.")
    return True


def main():
    """Run the interactive command-line contact manager."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            if not name or not phone:
                print("Contact name and phone number cannot be empty.")
                continue
            try:
                add_contact(name, phone)
            except DuplicateContactError as error:
                print(f"Error: {error}")
        elif choice == 2:
            name = input("Enter name to find: ").strip()
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            delete_contact(name)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
