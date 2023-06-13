import random
from statistics import mean, median, mode

high_score = 0 
guesses_list = []


def start_game():
    global high_score
    global guesses_list

    print("Hello, Player, please select a number between 0 and 100")
    
         

    answer = random.randint(0, 100)
    attempt_count = 0

    if high_score < 1:
        print("Currently no high score recorded")
    else:
        print(f'Current highs score is "{high_score}" attempts')
        print("Choose a number between 0 and 100")

    
    while True:
        try:
                 player_guess = int(input("> "))
                 if player_guess < 0 or player_guess > 100:
                    raise Exception("Sorry invalid guess, please choose a number between 0 and 100, tyr again")
        except ValueError:
                print("Please enter a whole number")
                continue
        except Exception as e:
                 print(f"{e}")
                 continue
        if player_guess > answer:
                print("Too high, try again")
                attempt_count +=1
                continue
        elif player_guess < answer:
                print("Too low, try again")
                attempt_count +=1
                continue
        else:
                attempt_count +=1
                print(f'That is correct, you guessed the right number in "{attempt_count}" attempt(s), great job!')
                guesses_list.append(attempt_count)
                if attempt_count > high_score:
                    high_score = attempt_count
                print("Here are your statistics for the game")
                min_number = min(guesses_list)
                print(f"Your min is:   {min_number}")
                max_number = max(guesses_list)
                print(f"Your max is:    {max_number}")
                player_mean = mean(guesses_list)
                print(f"Your total average is:    {player_mean}")
                player_median = median(guesses_list)
                print(f"Your median is:    {player_median}")
                player_mode = mode(guesses_list)
                print(f"Your mode is:    {player_mode}")

                 
                print("Would you like to play again? Y/N    ")
                proceed = input()
        if proceed.lower() == 'y':
                    start_game()
        elif proceed.lower() == 'n':
                print("Thanks for trying the number guessing game, hope you enjoyed it!")
            
                        
        else: 
                print("Sorry that was a invalid responce, please enter a Y or N")
                continue
               

    

start_game()


