#twig willaims
# 10/27/23
# assignment_four.py
# simulates and plays a game of 21(blackjack) with the user

import random


def get_card():
    """
    Generates a random card value between 1 and 10.
    Returns:
        int: A random card value between 1 and 10.
    """
    return random.randint(1, 10)


def get_winner(user_total, dealer_total):
    """
    Determines the winner of the game based on the user's and dealer's card totals.
    Args:
        user_total (int): The total value of the user's cards.
        dealer_total (int): The total value of the dealer's cards.
    Returns:
        str: A message indicating who won the game or if it's a tie.
    """
    if user_total > 21:
        return "Dealer wins! Your total is over 21."
    elif dealer_total > 21 or user_total > dealer_total:
        return "You win!"
    elif user_total == dealer_total:
        return "It's a tie!"
    else:
        return "Dealer wins."


def main():
    """
    Runs a '21' card game where the user competes against a dealer.
    """
    # Initialize user and dealer card totals
    user_total = get_card() + get_card()
    print(f"Your total is: {user_total}")

    # User's turn: keep asking for another card until user decides to stop or goes over 21
    while user_total < 21:
        another_card = input("Do you want another card? (yes/no): ").lower()
        if another_card == "yes":
            user_total += get_card()
            print(f"Your total is now: {user_total}")
        else:
            break

    # Determine if the user has won or lost
    if user_total > 21:
        print("You lost! Your total is over 21.")
    else:
        # Dealer's turn: determine dealer's total and display it
        dealer_total = get_card() + get_card()
        print(f"Dealer's total is: {dealer_total}")

        # Dealer takes another card if the total is less than 17
        while dealer_total < 17:
            dealer_total += get_card()
            print(f"Dealer takes another card. Dealer's total is now: {dealer_total}")

        # Determine and display the game result
        result = get_winner(user_total, dealer_total)
        print(result)


if __name__ == "__main__":
    main()
