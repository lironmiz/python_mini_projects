import random
from ascii_art import rock, paper, scissors
def main():
  print(f"welcome to liron rock paper scissors game! \U0001F604")
  game_images = [rock, paper, scissors]
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
  else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    victory_check(user_choice, computer_choice)
   
def victory_check(user_choice: int, computer_choice: int) -> None:
  """
    chack whe is won the game
    Input: user_choice: int, computer_choice: int
    Returns: None
  """
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")

if __name__ == "__main__":
    main()
