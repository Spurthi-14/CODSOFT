import random
print("===== ROCK PAPER SCISSORS GAME =====")
user_score = 0
computer_score = 0
tie_score = 0
while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        print("It's a Tie!")
        tie_score += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Win!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
    print("\nCurrent Score")
    print("You:", user_score)
    print("Computer:", computer_score)
    print("Ties:", tie_score)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("\n===== FINAL SCORE =====")
print("You:", user_score)
print("Computer:", computer_score)
print("Ties:", tie_score)
print("\nThanks for playing!")