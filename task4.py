def parse_input(command):
    cmd, *args = command.strip().lower().split()
    return cmd, args
def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Usage: add <name> <phone>"
    name, phone = args
    if name in contacts:
        return f"Contact '{name}' already exists. Updating phone number."
    contacts[name] = phone
    return "Contact added."
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Usage: change <name> <new_phone>"
    name, new_phone = args
    if name not in contacts:
        return f"Error: Contact '{name}' does not exist."
    contacts[name] = new_phone
    return "Contact updated."
def show_contact(args, contacts):
    if len(args) != 1:
        return "Error: Invalid number of arguments. Usage: phone <name>"
    name = args[0]
    if name not in contacts:
        return f"Error: Contact '{name}' does not exist."
    return f"{name}: {contacts[name]}"
def show_all_contacts(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        if not lines:
            return "No contacts available."
        result = "Contacts:"
        for line in lines:
            if line.strip() and not line.lower().startswith("mobile phones"):
                result += f"\n{line.strip()}"
        return result
    except FileNotFoundError:
        return "Error: The contacts file does not exist."
def main():
    contacts = {}
    print("Welcome to the assistant bot! Please enter 'hello' or 'exit'")
    while True:
        command = input("Enter a command: ").strip().lower()
        cmd, *args = parse_input(command)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you? Enter 'phone', 'change', 'show', 'username' or 'exit'")
        elif command == "change":
            def change_phone_number(path, name, new_phone):
                try:
                    with open(path, "r", encoding ="utf-8") as file:
                        lines = file.readlines()
                    contact_found = False
                    for i, line in enumerate(lines):
                        if line.strip().lower().startswith(name.lower() +":"):
                            lines[i]= f"{name}:{new_phone}\n"
                            contact_found = True
                    if not contact_found:
                        print(f"Error: Contact '{name}' not found in the phonebook.")
                        return
                    with open(path, "w", encoding="utf-8") as file:
                        file.writelines(lines)
                    print(f"Phone number for {name} updated successfully.")
                except FileNotFoundError:
                    print("Error: File not found. Please check the file path.")
            name = input("Enter the name and surname of the contact to modify: ")
            new_phone = input("Enter the new phone number: ")
            path = "phones.txt"
            change_phone_number(path, name, new_phone)
        elif command == "username":
            def find_username(path, name):
                try:
                    with open(path, "r", encoding = "utf-8") as file: 
                        lines = file.readlines()
                    for line in lines:
                        if line.strip().lower().startswith(name.lower() + ":"):
                            _, phone_number = line.strip().split(":", 1)
                            return f"The phone number for {name} is {phone_number.strip()}"
                except FileNotFoundError: 
                    print("Error: File not found. Please check the file path.")
            path = "phones.txt"
            name = input("Enter the name you're searching for:")
            print(find_username(path, name))
        elif command == "phone":
            def phonebook(path, name, phone):
                try:
                    with open(path, "a", encoding="utf-8") as file:
                        file.write(f"{name}:{phone}\n")
                        print(f"Phone number for {name} added successfully")
                except FileNotFoundError:
                    print("Error: Invalid number of arguments.")
            name = input("Enter your name and surname:")
            phone = input("Enter your phone number: ")
            path = "phones.txt"
            phonebook(path, name, phone)
        elif command == "show":
            file_path = "phones.txt"
            print(show_all_contacts(file_path))
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()
