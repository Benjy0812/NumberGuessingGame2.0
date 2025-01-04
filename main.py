import random
import os


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
        except ValueError:
            clear_console()
            input("Error: please enter a valid number between (1-5)"
                  "\nPress enter to continue ")
            clear_console()


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
            print("Error: Please enter a valid number between "
                  f"(1-{difficulty}) ")


def start_guessing():
    difficulty_choice = get_difficulty_level()
    clear_console()
    user_input(difficulty_choice)
    while True:
        try:
            user_exit = input("\ndo you want to play again? (yes/no): "
                              ).lower().strip()
            if user_exit == 'no':
                print("Good bye!")
                break
            elif user_exit == 'yes':
                start_guessing()
            elif user_exit != 'yes' and user_exit != 'no':
                clear_console()
                input("Error: you can only enter (yes-no)"
                      "\nPress enter to continue")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    start_guessing()
