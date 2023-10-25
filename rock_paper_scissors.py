# twig williams
# starts a rps game with user
import random

def who_wins(user, computer):
    if user == computer:
        return "How did you choose what I chose?, we tied!"
    elif user == 1 and computer == 3 or user == 2 and computer == 1 or user == 3 and computer == 2:
        return "Dang you win!, I but dont worry I will beat you next time!"
    else:
        return "I win!, better luck next time."

def main():
    user = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
    if user < 1 or user > 3:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    computer = random.randint(1, 3)
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    print(f"You have chosen {choices[user]}")
    print(f"I have chosen {choices[computer]}")

    result = who_wins(user, computer)
    print(result)

if __name__ == "__main__":
    main()
