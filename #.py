#.py

def main():
      # empty dictionary to store student information
      students = {}

      # add students using names as keys
      students = {
            "Jennifer":{  
                  "ID": "001",
                  "GPA": 3.8,
                  "credits-completed": 45,
                  "Grades": ["A", "B+", "A-", "A"]
            },
            "Edward":{
                  "ID": "002",
                  "GPA": 3.4,
                  "credits-completed": 60,
                  "Grades": ["B", "B", "A","C+"]
            }
      }
      

      #print dictionary
      print(students)
      print()

      #print student names
      print("STUDENT NAMES:")
      for name in students:
            print(name)
      print()

      # Student Information format
      print("STUDENT INFORMATION ")
      print("Student\tID\tGPA\tCredits Completed\tGrades") #used escape character found in W3 schools
      print("-------------------------------------------------")
      for name, info in students.items():
            print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['credits-completed']}\t{info['Grades']}")
      print()

      # print dictionary values in a loop
      print("ACCESSING STUDENT INFO USING THE KEY IN A LOOP")
      for name in students:
            print(name, students[name])
      print()

      #remove Jennifer from dictionary
      print("Jennifer has dropped out, removing from student info registry.")
      students.pop("Jennifer", None)
      print(students)
      print()

      #Access Edward's GPA    
      print("Getting Edward's GPA")
      print(students["Edward"]["GPA"])
      print()

      #clear dictionary
      print("Students have graduated, clearing the student registry.")
      students.clear()
      print(students)

      print("Completed by Jennifer Mendoza Trejo")

# running main function
if __name__ == "__main__":
      main()
      
