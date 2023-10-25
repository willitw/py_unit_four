import random

random_number = random.randint(1, 10)

user_guess = int(input("WHAT IS UP! GUESS THE NUMBER THAT IM THINKING OF: "))

if user_guess == random_number:
    print("YOU MUST BE CHEATING YOU GUESSED IT")
else:
    difference = abs(random_number - user_guess)
    print(f"HAHAHA YOU GOT IT WRONG MY NUMBER WAS, {random_number}. YOU ARE SO BAD YOU WERE {difference} AWAY FROM IT.")