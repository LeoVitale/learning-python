# Contact Manager with Type Annotations

from typing import List, Dict, Union

contacts: List[Dict[str, object]] = []


def display_menu() -> str:
    print("\n=== CONTACT MANAGER ===")
    print("1. Add contact")
    print("2. View contact list")
    print("3. Edit contact")
    print("4. Mark/Unmark contact as favorite")
    print("5. View favorite contacts")
    print("6. Delete contact")
    print("7. Exit")
    option: str = input("Choose an option: ")
    return option


def add_contact() -> None:
    print("\n=== ADD CONTACT ===")
    name: str = input("Name: ")
    phone: str = input("Phone: ")
    email: str = input("Email: ")
    favorite_input: str = input("Mark as favorite? (y/n): ").lower()
    favorite: bool = favorite_input == "y"
    contact: Dict[str, object] = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": favorite,
    }
    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts() -> None:
    print("\n=== CONTACT LIST ===")
    if not contacts:
        print("No contacts registered.")
    else:
        for i, contact in enumerate(contacts):
            fav: str = " (Favorite)" if contact["favorite"] else ""
            print(
                f"{i + 1}. {contact['name']}{fav} - {contact['phone']} - {contact['email']}"
            )


def edit_contact() -> None:
    view_contacts()
    if contacts:
        try:
            index: int = (
                int(input("Enter the number of the contact you want to edit: ")) - 1
            )
            if 0 <= index < len(contacts):
                contact: Dict[str, Union[str, bool, object]] = contacts[index]
                print(f"\nEditing contact: {contact['name']}")
                new_name: str = input(f"New name ({contact['name']}): ") or str(
                    contact["name"]
                )
                new_phone: str = input(f"New phone ({contact['phone']}): ") or str(
                    contact["phone"]
                )
                new_email: str = input(f"New email ({contact['email']}): ") or str(
                    contact["email"]
                )
                contact["name"] = new_name
                contact["name"] = new_name
                contact["phone"] = new_phone
                contact["email"] = new_email
                print("Contact updated successfully!")
            else:
                print("Contact not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def toggle_favorite() -> None:
    view_contacts()
    if contacts:
        try:
            index: int = (
                int(
                    input(
                        "Enter the number of the contact you want to mark/unmark as favorite: "
                    )
                )
                - 1
            )
            if 0 <= index < len(contacts):
                contact: Dict[str, object] = contacts[index]
                contact["favorite"] = not contact["favorite"]
                state: str = "favorite" if contact["favorite"] else "not favorite"
                print(f"Contact marked as {state}.")
            else:
                print("Contact not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def view_favorites() -> None:
    print("\n=== FAVORITE CONTACTS ===")
    favorites: List[Dict[str, object]] = [c for c in contacts if c["favorite"]]
    if not favorites:
        print("No favorite contacts.")
    else:
        for contact in favorites:
            print(f"- {contact['name']}")


def delete_contact() -> None:
    view_contacts()
    if contacts:
        try:
            index: int = (
                int(input("Enter the number of the contact you want to delete: ")) - 1
            )
            if 0 <= index < len(contacts):
                contact: Dict[str, object] = contacts.pop(index)
                print(f"Contact {contact['name']} deleted successfully!")
            else:
                print("Contact not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main() -> None:
    while True:
        option: str = display_menu()
        if option == "1":
            add_contact()
        elif option == "2":
            view_contacts()
        elif option == "3":
            edit_contact()
        elif option == "4":
            toggle_favorite()
        elif option == "5":
            view_favorites()
        elif option == "6":
            delete_contact()
        elif option == "7":
            print("Exiting the contact manager. See you later!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
