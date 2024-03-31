# This game was built using GitHub Copilot, but notably the code
# matches this website's version almost identically:
#   https://realpython.com/python-rock-paper-scissors/

import random

def play_game():
user_action = input("Enter throw (rock, paper, scissors): ")
ai_action = random.choice(["rock", "paper", "scissors"])

print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

if user_action == ai_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if ai_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if ai_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if ai_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

#Allow the user to play the game repeatedly until they decide to quit.
while true:
    play_game()
    play_again = input("Do you want to play the game again? (y/n): ")
    if play_again.lower() != "y":
        break
