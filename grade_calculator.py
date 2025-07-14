# grade_calculator.py
import random

def main():
    # empty list to store grades
    grades = []

    # Get grades using while loop
    while True:
        user_input = input("Enter a grade or -1 to stop: ")
        if user_input == "-1":
            break
        try:
            grade = float(user_input)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Print entered grades
    print("Grades entered:", grades)

    # Remove the lowest grade
    print("REMOVING THE LOWEST GRADE")
    if grades:
        lowest_grade = min(grades)
        lowest_index = grades.index(lowest_grade)
        grades.pop(lowest_index)
        print("Updated grades:", grades)
    else:
        print("No grades to remove.")

    # Remove a random grade
    print("REMOVING A RANDOM GRADE")
    if grades:
        random_grade = random.choice(grades)
        grades.remove(random_grade)
        print("Removed grade:", random_grade)
        print("Updated grades:", grades)
    else:
        print("No grades to remove.")

    # Edit a grade
    print("EDITING A GRADE")
    if grades:
        index = 0
        while index < count_items(grades):
            print(str(index + 1) + ":", grades[index])
            index = index + 1

        while True:
            try:
                user_choice = int(input("Which grade would you like to edit? (enter number): "))
                if user_choice < 1 or user_choice > count_items(grades):
                    print("Invalid number. Try again.")
                else:
                    new_value = float(input("Enter the new grade: "))
                    grades[user_choice - 1] = new_value
                    break
            except ValueError:
                print("Invalid input. Try again.")

        print("Updated grades:", grades)
    else:
        print("No grades to edit.")

    # Sort and reverse
    print("--- Sorting and reversing the list ---")
    grades.sort()
    grades.reverse()
    print("Sorted and reversed grades:", grades)

    # Total and average
    print("GRADE TOTAL & AVERAGE")
    total_score = sum(grades)
    number_of_grades = count_items(grades)
    if number_of_grades > 0:
        average_score = total_score / number_of_grades
    else:
        average_score = 0
    print("Total:", total_score)
    print("Average:", average_score)

    print("Completed by, Jennifer Mendoza Trejo")

# Manual function to count items 
def count_items(grade_list):
    counter = 0
    for item in grade_list:
        counter = counter + 1
    return counter

if __name__ == "__main__":
    main()

