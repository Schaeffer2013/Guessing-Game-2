import math
import random
import sys
from statistics import mean, median, mode, multimode


def start_game():

    print("Hello, Player, please choose a number between 0 and 100")

    answer = random.randint(0, 100)
    number_of_guesses = []

    while answer:
            try: 
                player_guess = int(input("> "))
                if player_guess < 0 or player_guess > 100:
                    raise ValueError
            except ValueError as err:
                print("Sorry invalid guess, please choose a number between 1 and 100, tyr again".format(err))
            else:
                print("")
            if player_guess > answer:
                print("Too high, try again")
                number_of_guesses.append(player_guess)
                continue
            elif player_guess < answer:
                print("Too low, try again")
                number_of_guesses.append(player_guess)
                continue
            else:
                 print("That is correct, you guessed the right number in {} attempt(s), great job!".format(len(number_of_guesses)))

                 print("Would you like to play again? Y/N    ")
                 proceed = input()
                 while proceed:
                            if proceed.lower() == 'y':
                                start_game()
                            elif proceed.lower() == 'n':
                                break
                 print("Thanks for trying the number guessing game, hope you enjoyed it!")
                 break
            
    print("Here are your statistics for the game")
    min_number = min(number_of_guesses)
    print(f"The lowest number you guessed was:   {min_number}")
    max_number = max(number_of_guesses)
    print(f"The highest number you guessed was:    {max_number}")
    player_mean = mean(number_of_guesses)
    print(f"The average of all your guesses is:    {player_guess}")
    player_median = median(number_of_guesses)
    print(f"The middle number you guessed was:    {player_median}")
    player_mode = mode(number_of_guesses)
    print(f"The most frequent number you guessed was:    {player_mode}")

    

start_game()


