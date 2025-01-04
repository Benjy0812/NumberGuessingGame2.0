import random
import os

# Function to clear the console based on the operating system


def clear_console():
    if os.name == "nt":
        os.system("cls")  # Windows
    else:
        os.system("clear")  # Unix/Linux/MacOS


def print_error_message(message):
    input(f"Error: {message}\nPress enter to continue.")


def get_difficulty_level():
    while True:
        try:
            print("Choose the difficulty level:")
            print("1. Easy (1-10)")
            print("2. Medium (1-25)")
            print("3. Hard (1-50)")
            print("4. Very Hard (1-100)")
            print("5. Super Hard (1-1000)")

            difficulty_choice = int(input("Difficulty: "))

            difficulty_mapping = {
                1: 10,
                2: 25,
                3: 50,
                4: 100,
                5: 1000,
            }

            if difficulty_choice in difficulty_mapping:
                return difficulty_mapping[difficulty_choice]
            else:
                print_error_message(
                    "Please enter a valid number between 1 and 5.")
        except ValueError:
            print_error_message("Please enter a valid number between 1 and 5.")


def user_input(difficulty):
    random_number = random.randint(1, difficulty)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {difficulty}: "))
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
            print(f"Error: Please enter a valid number between 1 and {
                  difficulty}.")


def start_guessing():
    difficulty_choice = get_difficulty_level()
    clear_console()
    user_input(difficulty_choice)

    while True:
        user_exit = input(
            "\nDo you want to play again? (yes/no): ").lower().strip()

        if user_exit == 'no':
            print("Goodbye!")
            break
        elif user_exit == 'yes':
            clear_console()
            break
        else:
            print_error_message("You can only enter 'yes' or 'no'.")


if __name__ == "__main__":
    start_guessing()
