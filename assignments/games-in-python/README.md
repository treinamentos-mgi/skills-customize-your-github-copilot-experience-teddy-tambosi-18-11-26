
# 📘 Assignment: Games in Python

## 🎯 Objetivo

Build a Hangman game in Python to practice strings, loops, conditionals, random selection, and user input. The player guesses a hidden word before running out of incorrect guesses.

## 📝 Tarefas

### 🛠️ Build the Hangman Game

#### Descrição
Create a command-line Hangman game that selects a word from a predefined list and lets the player guess letters until they win or run out of attempts.

#### Requisitos
O programa concluído deve:

- Select a word randomly from a predefined list.
- Display each unguessed letter as an underscore and reveal correctly guessed letters in their positions.
- Track and display the number of incorrect guesses remaining, starting with a limit of six.
- End the game when the player reveals the whole word or uses all six incorrect guesses.
- Display the correct word and a clear win or loss message when the game ends.

### 🛠️ Validate Guesses and Give Feedback

#### Descrição
Handle player input consistently so invalid or repeated guesses do not make the game unfair or confusing.

#### Requisitos
O programa concluído deve:

- Accept guesses without regard to letter case.
- Require each guess to be a single alphabetic character; prompt again when the input is invalid.
- Keep track of guessed letters and show them to the player.
- Notify the player when they repeat a guess without reducing the remaining attempts.