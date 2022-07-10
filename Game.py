import random

greeting_statement = "\nWelcome to Rock, Paper and Scissors Game!"
ending_statement = "Thank you for playing our game"
loss_statement = "You Lost. Better Luck Next Time"
win_statement = "You have Won!"


def stars():
    i = 0
    while i < 50:
        print("*", end="")
        i += 1


def game_algo():
   computer_move = random.choice(["rock", "paper", "scissors"])
   return computer_move


stars()
print(greeting_statement)
print("")

while True:
    ask = input("Would you like to play the game? (yes/no): ").lower()
    if ask == "yes":
        break
    elif ask == "no":
        quit()
    else:
        print("Sorry I could not understand")


while True:
    game_choice = input("Rock, Paper or Scissors?:").lower()
    if (game_choice == game_algo()):
        print("It's a tie")
        print(ending_statement)
        break
    elif (game_choice == "scissors" and game_algo() == "rock") or (game_choice == "paper" and game_algo() == "scissors") or (game_choice == "rock" and game_algo() == "paper"):
        print(loss_statement)
        print(ending_statement)
        break
    elif (game_choice == "scissors" and game_algo() == "paper") or (game_choice == "paper" and game_algo() == "rock") or (game_choice == "rock" and game_algo() == "scissors"):
        print(win_statement)
        print(ending_statement)
        break
    else:
        print("Sorry I could not understand. Kindly re-enter your choice")
