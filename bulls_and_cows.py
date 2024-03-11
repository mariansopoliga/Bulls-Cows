# TODO Header
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Marian Sopoliga
email: sopoligamarian@gmail.com
discord: Marian S.
"""

# TODO import
import os
import random
import time

# TODO Greet the user and print the introductory text
def greet_user():
    """
    Greets the user and prints the introductory text.

    This function clears the console screen, prints a greeting message,
    and provides an introductory text for the Bulls and Cows game.
    """
    os.system('cls')
    greeting = "I've generated a random 4-digit number for you."
    separator = "-" * len(greeting)
    print(
        "Hi there!",
        "",
        greeting,
        separator,
        "Let's play a bulls and cows game.",
        separator, sep="\n"
    )


# TODO Generate a secret 4-digit number
def generate_secret_number():
    """
    Generates a secret 4-digit number for the user to guess.

    This function randomly generates a 4-digit number with unique digits.

    Returns:
        str: The secret 4-digit number.
    """
    secret_number_str = ""
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    secret_number = digits[:4]
    for digit in secret_number:
        secret_number_str += str(digit)
    print(secret_number_str)  # for testing purposes
    return secret_number_str


# TODO Player guesses a number
def guess_number(guess):
    """
    Checks if the user's guess is valid (a 4-digit number).

    This function validates if the user's guess is a 4-digit number with unique digits.

    Parameters:
        guess (str): The user's guess.

    Returns:
        bool: True if the guess is valid, False otherwise.
    """
    if len(guess) != 4 or not guess.isdigit():
        return False
    if len(set(guess)) != 4 or guess[0] == '0':
        return False
    return True


# TODO Evaluate the guess
def evaluate_guess(secret, guess):
    """
    Evaluates the user's guess and returns the number of bulls and cows.

    This function compares the user's guess with the secret number and counts the number of bulls and cows.

    Parameters:
        secret (str): The secret 4-digit number.
        guess (str): The user's guess.

    Returns:
        tuple: A tuple containing the number of bulls and cows.
    """
    bulls = count_bulls(secret, guess)
    cows = count_cows(secret, guess)
    return bulls, cows


def count_bulls(secret, guess):
    """
    Counts the number of bulls in the user's guess.

    This function compares each digit of the user's guess with the corresponding digit in the secret number.
    A bull is counted if the digit matches exactly.

    Parameters:
        secret (str): The secret 4-digit number.
        guess (str): The user's guess.

    Returns:
        int: The number of bulls.
    """
    bulls = 0
    for index, s_digit in enumerate(secret):
        if s_digit == guess[index]:
            bulls += 1
    return bulls


# TODO Count cows
def count_cows(secret, guess):
    """
    Counts the number of cows in the user's guess.

    This function counts the number of digits in the user's guess that exist in the secret number,
    but are not in the correct position.

    Parameters:
        secret (str): The secret 4-digit number.
        guess (str): The user's guess.

    Returns:
        int: The number of cows.
    """
    secret_digit_counts = {}
    guess_digit_counts = {}
    cows = 0

    for index, digit in enumerate(secret):
        if digit == guess[index]:
            continue
        if digit not in secret_digit_counts:
            secret_digit_counts[digit] = 0
        secret_digit_counts[digit] += 1

        if guess[index] not in guess_digit_counts:
            guess_digit_counts[guess[index]] = 0
        guess_digit_counts[guess[index]] += 1

    for digit in set(secret):
        if digit in secret_digit_counts and digit in guess_digit_counts:
            cows += min(secret_digit_counts[digit], guess_digit_counts[digit])

    return cows


# TODO Counting how long it takes the user to guess the secret number
def guess_time(start_time, end_time):
    """
    Calculates and returns the time taken by the user to guess the secret number.

    This function calculates the difference between the end time and start time,
    and formats it into a human-readable string.

    Parameters:
        start_time (float): The start time of the game.
        end_time (float): The end time of the game.

    Returns:
        str: A string representing the time taken by the user to guess the secret number.
    """
    guessing_time = end_time - start_time
    minutes = int(guessing_time // 60)
    seconds = int(guessing_time % 60)
    return f"{minutes} minutes and {seconds} seconds"


# TODO Guess feedback
def guess_feedback(num_guesses):
    """
    Provides feedback based on the number of guesses made by the user.

    This function categorizes the user's performance based on the number of guesses made.
    If the number of guesses is less than or equal to 5, it's considered amazing.
    If the number of guesses is between 6 and 10, it's considered average.
    If the number of guesses is more than 10, it's considered not so good.

    Parameters:
        num_guesses (int): The number of guesses made by the user.

    Returns:
        str: Feedback based on the number of guesses.
    """
    if num_guesses <= 5:
        return "amazing!"
    elif 6 <= num_guesses <= 10:
        return "average."
    else:
        return "not so good."



# TODO Main function
def main():
    """
    The main function to run the Bulls and Cows game.

    This function orchestrates the gameplay, including greeting the user, generating a secret number,
    accepting user guesses, evaluating guesses, and providing feedback to the user.
    """
    greet_user()
    secret_number = generate_secret_number()
    num_guesses = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ")
        if not guess_number(guess):
            print("Invalid input. Please enter a 4-digit number with unique digits and the first digit not being 0.")
            continue
        num_guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        if bulls == 4:
            end_time = time.time()
            print(
            f"Correct, you've guessed the right number in {num_guesses} {'guess' if num_guesses == 1 else 'guesses'} !",
            f"That's {guess_feedback(num_guesses)}",
            f"Time taken to guess the number: {guess_time(start_time, end_time)}",
            sep="\n"
            )
            break

        else:
            # List the number of bull/bulls or cow/ cows
            print(
                f"{bulls} {'bull' if bulls == 1 else 'bulls'} "
                f"and {cows} {'cow' if cows == 1 else 'cows'}. Try again."
            )


if __name__ == "__main__":
    main()
