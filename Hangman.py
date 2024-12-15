import random

def print_welcome_message():
    print("Welcome to the game Hangman")
    print(" _    _ ")
    print("| |  | |")
    print("| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __")
    print("|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\")
    print("| |  | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|")
    print("                     __/ |")
    print("                    |___/")
    print("")


def print_hangman_picture(stage):
    hangman_stages = [
        """
        x-------x
        """,
        """
        x-------x
        |
        |
        |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
    ]
    print(hangman_stages[stage])


def main():
    print_welcome_message()

    attempts = 6
    print(f"Remaining attempts: {attempts}")

    for stage in range(7):
        print(f"Stage {stage + 1}:")
        print_hangman_picture(stage)
        print("")


if __name__ == "__main__":
    main()

print("Daniel\nMerhasin")

