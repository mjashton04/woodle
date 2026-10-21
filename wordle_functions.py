#Create and use custom functions in wordle_functions.py. Your program should include the
#functions:
#• choose_word() – Selects and returns a secret word.
import random


def choose_word():
    # List of five-letter words
    words = [
    "acorn",
    "blush",
    "champ",
    "drive",
    "frost",
    "glyph",
    "heavy",
    "ivory",
    "jumbo",
    "knife",
    "latch",
    "might",
    "noble",
    "prick",
    "quick",
    "ranch",
    "stomp",
    "tiger",
    "uncle",
    "vapor",
    "wreck",
    "zebra",
    "bread",
    "flock",
    "sting",
]
    # Randomly select a word from the list
    secret_word = random.choice(words)
    return secret_word
#• get_guess() – Gets and validates the player’s guess.
def get_guess(previous_guesses):
    while True:
        guess = input("Enter your guess (five-letter word): ").lower()
        if len(guess) != 5:
            print("Brother what part of 5 letters don't you understand? Please enter a FIVE-LETTER word.")
        elif guess in previous_guesses:
            print("They say that doing the same thing over and over again and expecting different results is the definition of insanity. So how about you try something different.")
        else:
            return guess
#• evaluate_guess() – Compares the guess with the secret word and returns feedback.
def evaluate_guess(guess, secret_word):
    feedback = ""
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback += "G"  # Correct letter and position
        elif guess[i] in secret_word:
            feedback += "Y"  # Correct letter, wrong position
        else:
            feedback += "-"  # Letter is not in the word
    return feedback
#• display_guess() – Displays the guess and its feedback.
def display_guess(guess, feedback):
    print(f"Your guess:", " ".join(guess.upper()))
    print(f"Let's compare:", " ".join(feedback))
#• has_won() – Determines whether the player has guessed the word.
def has_won(feedback):
    return feedback == "GGGGG"
def play_again():
    while True:
        response = input("Would you like to play again? (yes/no): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Huh? Please enter 'yes' or 'no'.")