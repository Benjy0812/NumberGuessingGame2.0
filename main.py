import random
import os


def clear_console():
    os.system("cls")


def get_difficulty_level():
    print("Choose the difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-25)")
    print("3. Hard (1-50)")
    print("4. Very Hard (1-100)")
    print("5. Super Duper Hard (1-1000)")
    difficulty_choice = int(input("Difficulty: "))
    if difficulty_choice == 1:
        return 10
    elif difficulty_choice == 2:
        return 25
    elif difficulty_choice == 3:
        return 50
    elif difficulty_choice == 4:
        return 100
    elif difficulty_choice == 5:
        return 1000


def get_random_number(difficulty_choice):
    rand = random.randint(1, difficulty_choice)
    return rand


def user_input(random_number):
    try:
        guess = int(input(f"Enter your guess from 1 to {difficulty_choice}: "))

        if random_number == guess:
            print("You guessed right!")
        elif random_number < guess:
            print(f"You guessed over the random number was {random_number}")
        elif random_number > guess:
            print(f"You guessed under the random number was {random_number}")

    except ValueError:
        print("Please enter a valid number.")


# Main code flow
difficulty_choice = get_difficulty_level()
random_number = get_random_number(difficulty_choice)
clear_console()
user_input(random_number)
