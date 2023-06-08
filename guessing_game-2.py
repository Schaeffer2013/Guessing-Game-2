"""Psuedo-code Hints
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
import random
from statistics import mean, median, mode, multimode

min_number = 1
max_number = 100
random_number = random.randint(min_number, max_number)
guess_number = []

def start_game():
    start_game()
    print("Hello, Player")

    number = int(input("Choose a number between 1 and 100:    "))
    attempt_count = 1
    while guess_number != 0:
            try: 
                guess_number = int(input())
                if guess_number < 0 or guess_number > 100:
                    raise ValueError("Sorry invalid guess. Please pick a number between number between 1 and 50.")
        
                if guess_number > 8:
                    print("Too high, try again")
                    break
                elif guess_number < 8:
                    print("Too low, try again")
                    break
        
    print("That is correct, great job! Would you want to try again?   ")
    attempt_count += 1

answer = input




# Kick off the program by calling the start_game function.
start_game()
