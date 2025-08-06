import random

# Options
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit the game.\n")
while True:
    user_choice = input("Your move (rock/paper/scissors): ").lower()

    if user_choice == "exit":
        print("\n Thanks for playing!")
        print(f"Final Score: You {user_score} - {computer_score} Computer")
        break

    if user_choice not in choices:
        print(" Invalid choice! Please enter 'rock', 'paper', or 'scissors'.\n")
        continue

    computer_choice = random.choice(choices)
    print(f" Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = " You win!"
        user_score += 1
    else:
        result = " You lose!"
        computer_score += 1
    print(result)
    print(f"Score: You {user_score} - {computer_score} Computer\n")
