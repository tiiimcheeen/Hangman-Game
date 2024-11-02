# Hangman Game

A Python implementation of the classic Hangman game, allowing players to guess a word by selecting letters. This version includes adjustable difficulty levels and an external word list for added variety.

## Features

- **Three Difficulty Levels**: Choose between easy, medium, and hard, where difficulty determines the length of the word.
- **Random Word Selection**: Words are chosen randomly from an external file (`hangman_words.txt`).
- **ASCII Hangman Graphics**: Visual hangman graphics display with each incorrect guess.

## How to Play

1. Clone this repository or download the files.
2. Ensure `hangman.py` and `hangman_words.txt` are in the same directory.
3. Run the game with Python:
    ```bash
    python hangman.py
    ```
4. Follow the on-screen prompts to guess letters and try to reveal the word before reaching the maximum number of incorrect guesses.

## File Structure

- `hangman.py`: The main Python script that runs the game.
- `hangman_words.txt`: A text file containing a list of words for the game.

## Example Gameplay

```plaintext
Choose a difficulty level (easy, medium, hard): medium
**********
Current word: _ a _ _ _ _
Guessed letters: 
Enter a letter: e
```

## Customizing the Word List

To customize the game, you can add, remove, or modify words in `hangman_words.txt`. Each word should be on a new line.
