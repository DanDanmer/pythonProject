# from operator import index
#
# def print_welcome_message():
#     print("""\t\t\tWelcome to the game Hangman
#      _    _
#     | |  | |
#     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
#     |  __  |/ _ | '_ \\ / _ | '_  _ \\ / _ | '_ \\
#     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
#     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
#                          __/ |
#                         |___/
#     """)
#
# HANGMAN_PHOTOS = {
#     0: """
#     x-------x
#     """,
#     1: """
#     x-------x
#     |
#     |
#     |
#     |
#     |
#     """,
#     2: """
#     x-------x
#     |       |
#     |       0
#     |
#     |
#     |
#     """,
#     3: """
#     x-------x
#     |       |
#     |       0
#     |       |
#     |
#     |
#     """,
#     4: """
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |
#     |
#     """,
#     5: """
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      /
#     |
#     """,
#     6: """
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      / \\
#     |
#     """
# }
#
# def print_hangman(num_of_tries):
#     """
#     This function prints the current hangman state based on the number of wrong attempts.
#     :param num_of_tries: int - the number of wrong attempts made so far.
#     """
#     print(HANGMAN_PHOTOS[num_of_tries])
#
# def check_valid_input(letter_guessed, old_letters_guessed):
#     """
#     Check if the guessed letter is valid.
#
#     :param letter_guessed: str - the letter guessed by the user
#     :param old_letters_guessed: list - a list of letters guessed so far
#     :return: bool - True if the input is valid, False otherwise
#     """
#     # Check if the input is a single character and is an English letter
#     if len(letter_guessed) != 1 or not letter_guessed.isalpha():
#         return False
#
#     # Check if the letter was already guessed
#     if letter_guessed.lower() in old_letters_guessed:
#         return False
#
#     # The input is valid
#     return True
#
# def show_hidden_word(secret_word, old_letters_guessed):
#     return ' '.join([letter if letter in old_letters_guessed else '_' for letter in secret_word])
#
# def check_win(secret_word, old_letters_guessed):
#     # Verify that all letters in the secret word are in the list of guessed letters
#     for letter in secret_word:
#         if letter not in old_letters_guessed:
#             return False
#     return True  # this should be outside the for loop
#
# def choose_word(file_path, index):
#     """
#     Chooses a word from the file and returns the number of unique words and the chosen words
#     at the given index
#     :param file_path: "C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\words.txt"
#     :param index: The index of the word to choose
#     :return: A tuple with the count of unique words and the chosen word
#     """
#     with open(file_path, 'r') as file:
#         words = file.read().split()
#     # Remove duplicates
#     unique_words = set(words)
#     unique_count = len(unique_words)
#
#     # Adjust index to be 1-based and handle circular counting
#     adjusted_index = (index - 1) % len(words)
#     chosen_word = words[adjusted_index]
#
#     return unique_count, chosen_word
#
# def main():
#     print_welcome_message()
#
#     # The word is now chosen from the file automatically using the choose_word function
#     file_path = r"C:\Users\Daniel\PycharmProjects\pythonProject\words.txt"  # Use the raw string notation
#     index = 3  # The index of the word to choose (you can change it or make it random)
#
#     # Call the function to get the secret word and the count of unique words
#     unique_count, guess_word = choose_word(file_path, index)
#
#     print(f"Number of unique words: {unique_count}")
#     print(f"The secret word is: {guess_word}")
#
#     attempts = 6  # Number of allowed wrong guesses
#     current_stage = 0  # Hangman stage
#     old_letters_guessed = []  # Track previously guessed letters
#
#     print("\n" * 50)  # Clear the screen for Player 2.
#
#     # Game loop
#     while attempts > 0 and "_" in show_hidden_word(guess_word, old_letters_guessed):
#         # Use the show_hidden_word function to display progress
#         print(show_hidden_word(guess_word, old_letters_guessed))
#         print(f"Guessed letters: {', '.join(old_letters_guessed)}")
#         guess_letter = input("Guess a letter: ").lower()
#
#         if not check_valid_input(guess_letter, old_letters_guessed):
#             print("Invalid guess. Please try again")
#             continue
#
#         old_letters_guessed.append(guess_letter)
#
#         if guess_letter in guess_word:
#             print("Correct guess!")
#         else:
#             print("Wrong guess!")
#             attempts -= 1
#             current_stage += 1
#             print_hangman(current_stage)
#
#         print(f"Remaining attempts: {attempts}")
#
#     # Check if the player won or lost
#     if "_" not in show_hidden_word(guess_word, old_letters_guessed):
#         print(f"Congratulations! You won! The word was: {guess_word}")
#     else:
#         print(f"Game over! The word was: {guess_word}")
#
# if __name__ == "__main__":
#     main()

import os

# Constant for maximum tries
MAX_TRIES = 6

# Hangman stages
HANGMAN_PHOTOS = {
    0: "x------x",
    1: """x------x
|
|
|
|
|""",
    2: """x------x
|       |
|       0
|
|
|""",
    3: """x------x
|       |
|       0
|       |
|
|""",
    4: """x------x
|       |
|       0
|      /|\\
|
|""",
    5: """x------x
|       |
|       0
|      /|\\
|      /
|""",
    6: """x------x
|       |
|       0
|      /|\\
|      / \\
|"""
}

def clear_screen():
    """Clears the terminal screen. Works for both Windows and Unix-based systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    """Prints the welcome message."""
    print("""\t\t\tWelcome to the game Hangman
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _' | '_ \\ / _' | '_  _ \\ / _' | '_ \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                         __/ |
                        |___/
    """)
    print(f"Max incorrect guesses allowed: {MAX_TRIES}\n")

def get_game_parameters():
    """
    Prompts the user to enter the file path and index of the word.

    :return: Tuple containing the file path and index.
    :rtype: tuple(str, int)
    """
    while True:
        file_path = input("Please enter the path to the words file: ")
        if not os.path.isfile(file_path):
            print("Error: The file does not exist. Please enter a valid file path.")
            continue

        try:
            index = int(input("Please enter the index of the word: "))
            return file_path, index
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def choose_word(file_path, index):
    """
    Chooses a word from the file at the specified index.

    :param file_path: Path to the words file.
    :param index: Index of the desired word.
    :type file_path: str
    :type index: int
    :return: The chosen word.
    :rtype: str
    """
    with open(file_path, 'r') as file:
        words = file.read().split()
        if not words:
            print("The file is empty. Please provide a valid words file.")
            exit()

        unique_words = list(dict.fromkeys(words))  # Remove duplicates
        chosen_word = unique_words[(index - 1) % len(unique_words)]  # Handle index looping
    return chosen_word

def print_hangman(num_of_tries):
    """Prints the hangman stage based on the number of wrong guesses."""
    print(HANGMAN_PHOTOS[num_of_tries])

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the guessed letter is valid.

    :param letter_guessed: The letter guessed by the user.
    :param old_letters_guessed: List of previously guessed letters.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if input is valid, False otherwise.
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Tries to update the guessed letter list.

    :param letter_guessed: The letter guessed by the user.
    :param old_letters_guessed: List of previously guessed letters.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the letter was added, False otherwise.
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    old_letters_guessed.append(letter_guessed)
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    Displays the current state of the secret word.

    :param secret_word: The secret word to guess.
    :param old_letters_guessed: List of guessed letters.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: The current word display with guessed letters.
    :rtype: str
    """
    return " ".join([letter if letter in old_letters_guessed else "_" for letter in secret_word])

def check_win(secret_word, old_letters_guessed):
    """
    Checks if the player has guessed all the letters in the secret word.

    :param secret_word: The secret word to guess.
    :param old_letters_guessed: List of guessed letters.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if the player won, False otherwise.
    :rtype: bool
    """
    return all(letter in old_letters_guessed for letter in secret_word)

def main():
    """Main function to run the Hangman game."""
    clear_screen()
    print_welcome_message()

    file_path, index = get_game_parameters()
    secret_word = choose_word(file_path, index)
    old_letters_guessed = []
    num_of_tries = 0

    clear_screen()
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))

    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        guess_letter = input("Guess a letter: ").lower()

        if try_update_letter_guessed(guess_letter, old_letters_guessed):
            if guess_letter in secret_word:
                print("Good job! Keep going!")
            else:
                print(":(")
                num_of_tries += 1

        clear_screen()
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("Guessed letters:", " -> ".join(sorted(old_letters_guessed)))

    if check_win(secret_word, old_letters_guessed):
        print("WIN 🎉")
    else:
        print("LOSE 😢")
        print(f"The word was: {secret_word}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
