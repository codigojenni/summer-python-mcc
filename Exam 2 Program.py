import random

def create_employee(employee_list, existing_employee_ids, existing_employee_names):
    """
    Prompts for new employee name and generates a unique ID.
    Adds the new employee's data to the given lists.
    """
    while True:
        employee_name = input("Enter the employee's name: ")
        if employee_name.lower() in [name.lower() for name in existing_employee_names]:
            print(f"Error: An employee with the name '{employee_name}' already exists. Please enter a different name.")
        else:
            existing_employee_names = existing_employee_names + [employee_name]
            break

    while True:
        employee_id = random.randint(1, 500)
        if employee_id not in existing_employee_ids:
            # Using concatenation (list = list + [item])
            existing_employee_ids = existing_employee_ids + [employee_id]
            break

    employee = {"name": employee_name, "id": employee_id}
    employee_list = employee_list + [employee]

    # returns the updated lists
    return employee_list, existing_employee_ids, existing_employee_names


def output_employee_details(employee):
    """
    Prints formatted string for employee's name and ID.
    """
    print(f"Created employee: {employee['name']} with ID: {employee['id']}")


def main():
    """
    Main program to log and display new employee details.
    """
    print("Welcome to the Employee Logging Program!")

    # Initialize empty lists in main
    employee_log = []
    existing_employee_ids = []
    existing_employee_names = []

    while True:
        try:
            num_new_employees = int(input("Enter the amount of new employees being added to the organization: "))
            if num_new_employees < 0:
                print("Please enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    employees_added_count = 0
    while employees_added_count < num_new_employees:
        employee_log, existing_employee_ids, existing_employee_names = \
            create_employee(employee_log, existing_employee_ids, existing_employee_names)
        employees_added_count += 1

    print("\n--- Employee Details ---")
    # Loop through the employee_log
    for employee in employee_log:
        output_employee_details(employee)

    print("\nCompleted by Jennifer Mendoza Trejo")

if __name__ == "__main__":
    main()