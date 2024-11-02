"""
hangman.py

A Python implementation of the classic Hangman game. The player attempts to guess a randomly selected word
by guessing one letter at a time. The game allows players to choose from three difficulty levels
(easy, medium, hard), which adjusts the length of the word.

The word list is loaded from an external file, 'hangman_words.txt'. The game displays the current state
of the hangman figure after each incorrect guess, and players are given a limited number of wrong guesses.

Run this script to start the game and follow the on-screen instructions.
"""


import random

# Constants
WORDS_FILE = "hangman_words.txt"
MAX_WRONG_GUESSES = 6  # Keeping a fixed limit of wrong guesses

# ASCII art stages for the hangman
HANGMAN_ART = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}


def load_words(filename: str) -> list:
    """Load words from a file and return them as a list, ignoring blank lines."""
    try:
        with open(filename, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []


def display_man(wrong_guesses: int) -> None:
    """Display the hangman graphic based on the number of wrong guesses."""
    print("**********")
    for line in HANGMAN_ART[wrong_guesses]:
        print(line)
    print("**********")


def display_hint(hint: list) -> None:
    """Display the current hint with guessed letters revealed."""
    print("Current word:", " ".join(hint))


def display_result(answer: str, won: bool) -> None:
    """Display the final result, showing if the player won or lost."""
    print("\nThe word was:", " ".join(answer))
    if won:
        print("Congratulations, YOU WIN!")
    else:
        print("Game over, YOU LOSE!")
    print("=" * 20)


def select_difficulty() -> str:
    """Ask the player to select a difficulty level and return it."""
    while True:
        level = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if level in {"easy", "medium", "hard"}:
            return level
        print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")


def filter_words_by_difficulty(words: list, level: str) -> list:
    """Filter the words based on difficulty level."""
    if level == "easy":
        return [word for word in words if len(word) <= 5]
    elif level == "medium":
        return [word for word in words if 6 <= len(word) <= 8]
    return [word for word in words if len(word) >= 9]


def main() -> None:
    """Main function to run the Hangman game."""
    words = load_words(WORDS_FILE)
    play_again = True

    while play_again:
        level = select_difficulty()
        filtered_words = filter_words_by_difficulty(words, level)
        answer = random.choice(filtered_words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()

        while True:
            display_man(wrong_guesses)
            display_hint(hint)
            print("Guessed letters:", " ".join(sorted(guessed_letters)))

            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
                continue

            guessed_letters.add(guess)

            if guess in answer:
                for i, letter in enumerate(answer):
                    if letter == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_result(answer, won=True)
                break
            elif wrong_guesses >= MAX_WRONG_GUESSES:
                display_man(wrong_guesses)
                display_result(answer, won=False)
                break

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower() == "yes"


if __name__ == "__main__":
    main()
