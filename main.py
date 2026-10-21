
#• Import your functions from wordle_functions.py into main.py.
#• Include comments explaining important sections.
from wordle_functions import choose_word
from wordle_functions import get_guess 
from wordle_functions import evaluate_guess 
from wordle_functions import display_guess 
from wordle_functions import has_won
from wordle_functions import play_again

#• Use a list to store previous guesses.
previous_guesses = []
#• Use meaningful variable and function names.

#• Do not use classes or advanced Python features we have not discussed.


#Welcome the player.
print("Welcome to Mystery Wordle!")
print("    Guess the five-letter word.")
print("    G = correct letter and position")
print("    Y = correct letter, wrong position")
print("    - = letter is not in the word")
#2. Select a secret five-letter word.
secret_word = choose_word()
#3. Give the player up to six guesses.
max_attempts = 6
guess_count = 0
#4. Require each guess to contain exactly five letters.
#5. Reject guesses that have already been used.
while True:
    secret_word = choose_word()
    previous_guesses = []
    guess_count = 0
    while guess_count < max_attempts:
        print(f"Attempt {guess_count + 1} of {max_attempts}.")
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)
        guess_count += 1
        
        
        #7. Tell the player when a letter is correct, misplaced, or absent.

        feedback = evaluate_guess(guess, secret_word)
        
        #6. Display feedback after every guess.
            #After each guess, display feedback for every letter:
            #• G (Green) means the letter is correct and in the correct position.
            #• Y (Yellow) means the letter appears in the word but is in the wrong position.
            #• - means the letter does not appear in the word

        display_guess(guess, feedback)
        
        print()
        #8. End the game when the player guesses the word or uses all six attempts.
        if has_won(feedback):
            print(f"Congratulations! You've guessed the word '{secret_word}' in {guess_count} attempts.")
            break
        #9. Display the secret word if the player loses.
        if guess_count == max_attempts:
            print(f"You are out of attempts! The secret word was '{secret_word}'. Better luck next time!")
    #10. Ask whether the player would like to play again.
    play_again_choice = play_again()
    if not play_again_choice:
        print("Thanks for playing yo! Tchau!")
        break





