# rock_paper_scissors.py
from random import randrange

def main():
      # 'y' to enter loop
      play_again = "y"

      #loop to keep playing
      while play_again.lower() == "y":
            # get user/opponent weapon
            user_weapon = get_user_weapon()
            opponent_weapon = get_opponent_weapon()

            # show winner
            determine_winner(user_weapon, opponent_weapon)

            # ask user if they want to play again
            play_again = input("Do you want to play again? (y/n): ")
            print() 
      print("Thanks for playing!")
      print("Completed by, Jennifer Mendoza Trejo")
def get_user_weapon():
      print("Choose your weapon: ")
      print("1 - Rock")
      print("2 - Paper") 
      print("3 - Scissors")
      while True:
            try:  # from w3 schools
                  choice = int(input("Enter the number of your choice: ")) 
                  if choice in [1, 2, 3]: 
                        return choice
                  else:
                        print("Invalid choice. Please choose 1, 2, or 3.")
            except ValueError:
                  print("Please enter a valid number (1, 2, or 3).")                     
def get_opponent_weapon():
    # gives random number from 1 to 3
    return randrange(1, 4)

def determine_winner(user, opponent):
    weapons = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"\nYou chose {weapons[user]}")
    print(f"Opponent chose {weapons[opponent]}")

    if user == opponent:
        print("It's a tie!")
    elif (user == 1 and opponent == 3) or (user == 2 and opponent == 1) or (user == 3 and opponent == 2):
        print("You win!")
    else:
        print("You lose!")

# Only call main if this file is run directly
if __name__ == "__main__":
    main()           