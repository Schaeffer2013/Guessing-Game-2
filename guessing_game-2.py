import math
import random
import sys
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
                    raise ValueError
            except ValueError as err:
                print("Sorry invalid guess, please choose a number between 1 and 100, tyr again".format(err))
                continue
                if guess_number > random_number:
                    print("Too high, try again")
                    guess_number.append(number)
                    break
                elif guess_number < random_number:
                    print("Too low, try again")
                    guess_number.append(number)
                    break

     
    print("That is correct, you guessed the right number in {} attempts, great job! Would you like to try again?".format(len(guess_number)))

    while guess_number:
        if start_game.lower() == "y":
            continue
        elif start_game.lower == () == "n":
            print("Thanks for trying the number guessing game, hope you enjoyed it!")
            break
    attempt_count += 1
    min_number = min(guess_number)
    print(f"The lowest number guessed was:   {min_number}")
    max_number = max(guess_number)
    print(f"The highest number guessed was:    {max_number}")
    guess_mean = round.mean(guess_number)
    print(f"The average of all your guesses is:    {guess_mean}")
    guess_median = round.median(guess_number)
    print(f"The middle number you guessed was:    {guess_median}")
    guess_mode = round.mode(guess_number)
    print(f"The most frequent number you guessed was:    {guess_mode}")


