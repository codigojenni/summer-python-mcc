def get_string_input(prompt):
    return input(prompt)

def find_substring(main_str, sub_str):
    print("\nSearching for substring within the main string content, please wait!")
    print("-=------------------------------------------------------------------------")
    index = main_str.find(sub_str)
    if index != -1:
        print(f"{sub_str} was found in the main string at index {index}.")
    else:
        print(f"{sub_str} was not found in the main string.")
    return index

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def replace_substring(main_str, old_sub):
    print("Initiating the string replacement process!")
    print("--------------------------------------------")
    choice = get_yes_no(f"Do you want to replace '{old_sub}' with something else (y/n)? ")
    if choice == "y":
        new_sub = get_string_input("Enter the replacement string: ")
        updated_str = main_str.replace(old_sub, new_sub)
        print(f"New String: {updated_str}")
        return updated_str
    else:
        print("No replacement was made.")
        return main_str

def main():
    print("Welcome to the String Replacement Tool!")
    print("-------------------------------------------")

    main_string = get_string_input("Enter the string to search through: ")
    substring = get_string_input("Enter the string to search for: ")

    index = find_substring(main_string, substring)

    if index != -1:
        main_string = replace_substring(main_string, substring)

    print("Thank you for using our program!")
    print("Completed by, Jennifer Mendoza Trejo. ")

if __name__ == "__main__":
    main()
