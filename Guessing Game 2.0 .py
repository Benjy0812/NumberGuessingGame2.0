import random
import os


def clear_console():
    """
    Clears the console screen based on the operating system.
    """
    if os.name == "nt":
        os.system("cls")  # Windows
    else:
        os.system("clear")  # Unix/Linux/MacOS


def print_error_message(message):
    """
    Prints an error message and waits for user input before continuing.
    """
    input(f"Error: {message}\nPress enter to continue.")


def get_difficulty_level():
    """
    Prompts the user to select a difficulty level and returns the corresponding
    upper limit for the random number generation.
    """
    while True:
        try:
            print("Choose the difficulty level:")
            print("1. Easy (1-10) - Easy mode, perfect for beginners!")
            print("2. Moderate (1-25) - A bit of a challenge!")
            print("3. Challenging (1-50) - Only for brave guessers!")
            print("4. Hard (1-100) - A real test of skill!")
            print("5. Extreme (1-1000) - Prepare for a tough challenge!")

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
                print_error_message("Please enter a valid number between 1 and 5.")
        except ValueError:
            print_error_message("Please enter a valid number between 1 and 5.")


def user_input(difficulty):
    """
    Prompts the user to guess a number between 1 and the given difficulty level.
    The game continues until the user guesses correctly.
    """
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
                print("Too high! Try a smaller number.")
            elif guess < random_number:
                print("Too low! Try a larger number.")
        except ValueError:
            print("Error: Please enter a valid number between 1 and " f"{difficulty}.")


def start_guessing():
    """
    Starts the number guessing game, allowing the user to choose the difficulty
    and keep playing until they decide to exit.
    """
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    difficulty_choice = get_difficulty_level()
    clear_console()
    user_input(difficulty_choice)

    while True:
        user_exit = (
            input(
                "\nDo you want to play again? " "Type 'yes' to play or 'no' to exit: "
            )
            .strip()
            .lower()
        )

        if user_exit == "no":
            print("Goodbye! See you next time! 👋")
            break
        elif user_exit == "yes":
            clear_console()
            break
        else:
            print_error_message("You can only enter 'yes' or 'no'.")


if __name__ == "__main__":
    start_guessing()
