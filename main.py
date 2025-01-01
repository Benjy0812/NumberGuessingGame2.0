import os
import random


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_difficulty_level():
    while True:
        try:
            print("Choose the difficulty level:")
            print("1. Easy (1-10)")
            print("2. Medium (1-25)")
            print("3. Hard (1-50)")
            print("4. Very Hard (1-100)")
            print("5. Super Hard (1-1000)")
            difficulty_choice = int(input("Enter difficulty (1-5): "))
            if 1 <= difficulty_choice <= 5:
                ranges = {1: 10, 2: 25, 3: 50, 4: 100, 5: 1000}
                return ranges[difficulty_choice]
            else:
                clear_console()
                print("Invalid choice. Please select a valid difficulty level "
                      "(1-5).")
        except ValueError:
            clear_console()
            print("Error: Invalid input. Please enter a number.")


def play_guessing_game(max_range):
    random_number = random.randint(1, max_range)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_range}: "))
            attempts += 1

            if guess == random_number:
                print(f"🎉 You guessed it! The number was {random_number}.")
                print(f"It took you {attempts} attempts.")
                break
            elif guess > random_number:
                print("Too high! Try again.")
            elif guess < random_number:
                print("Too low! Try again.")
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    while True:
        clear_console()
        print("Welcome to the Number Guessing Game!")
        difficulty = get_difficulty_level()
        play_guessing_game(difficulty)

        user_exit = input("\nDo you want to play again? "
                          "(yes/no): ").strip().lower()
        if user_exit == 'no':
            print("Thanks for playing! Goodbye!")
            break
        elif user_exit != 'yes':
            print("Invalid input. Exiting the game.")
            break


if __name__ == "__main__":
    main()
