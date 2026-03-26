import random
import time

# Bankroll + Stats - cash the player has to bet with
bankroll = 1000
wins = 0
losses = 0
games_played = 0

## function to  take bet
def take_bet():
    while True:
        bet = int(input("How much do you want to bet? "))
        if bet < 50: # make a $50 minimum bet to avoid loop of small bets
            print("Minimum bet is $50. Please try again.")
        elif bet > bankroll: # make sure player cannot bet more than they have
            print("You cannot bet more than your current bankroll. Please try again.")
        elif bet % 50 != 0: # make sure bet is in increments of $50 to avoid small bets
            print("Bet must be in increments of $50. Please try again.")
        else:
            return bet

## 1. Coin Flip Game
def play_coin_flip(bankroll, wins, losses, games_played):
    bet = take_bet()    # take users bet

    choice = input("Choose heads or tails: ")
    if choice not in ["heads", "tails"]:            # makes sure user input is valid
        print("Invalid choice. Please try again.")
        return bankroll, wins, losses, games_played

     # simple for loop animation
    for i in range(2):
        print("Flipping...")
        time.sleep(0.8)

    #Results
    coin_flip = random.randint(0, 1)    # rng coin flip, 0 for heads, 1 for tails

    if coin_flip == 0:
        result = "heads"
    else:
        result = "tails"

    print("The coin flip result is:", result)

    games_played += 1

    if choice == result:    # if user guess is correct, they win, otherwise they lose
        print("You win!")
        bankroll += bet # 1:1 payout for coin flip
        wins += 1
    else:
        print("You lose!")
        bankroll -= bet
        losses += 1
    return bankroll, wins, losses, games_played



## 2. Dice Game
def play_dice_game(bankroll, wins, losses, games_played):
    bet = take_bet()    # take users bet

    dice_game = input("Select your bet type: 1 - Over/Under, 2 - Exact Number: ") # user selection

    ### 1. Over / Under
    if dice_game == "1":

        dice_roll = random.randint(1, 6) # rng dice roll between 1 and 6

        guess = input("Do you think the dice roll will be over or under 3.5? (over/under): ")
        if guess not in ["over", "under"]:
            print("Invalid choice. Please try again.")
            return bankroll, wins, losses, games_played

            # simple for loop animation
        for i in range(2):
            print("Rolling...")
            time.sleep(0.8)

        #Results
        print("The dice roll result is:", dice_roll)

        games_played += 1

        """ over 3.5 means 4, 5, or 6, under 3.5 means 1, 2, or 3"""
        if (guess == "over" and dice_roll > 3) or (guess == "under" and dice_roll < 4): 
            print("You win!")
            bankroll += bet # 1:1 payout for over/under dice game
            wins += 1
        else:
            print("You lose!")
            bankroll -= bet
            losses += 1


    ## 2. Exact Number
    elif dice_game == "2":

        guess = int(input("Guess the dice roll (1-6): ")) # user guesses the exact number on the dice roll, payout is 5:1 for guessing correctly

        if guess < 1 or guess > 6:                      # make sure user input is valid
            print("Invalid guess. Please try again.")
            return bankroll, wins, losses, games_played

        # simple for loop animation
        for i in range(2):
            print("Rolling...")
            time.sleep(0.8)

        #Results
        dice_roll = random.randint(1, 6)    # rng dice roll between 1 and 6

        print("The dice roll result is:", dice_roll)

        games_played += 1

        if guess == dice_roll:
            print("You win!")
            bankroll += bet * 5 # 5:1 payout for guessing the exact number on the dice
            wins += 1
        else:
            print("You lose!")
            bankroll -= bet
            losses += 1

    else:
        print("Invalid dice game choice.")
    return bankroll, wins, losses, games_played


## 3. Roulette
def play_roulette(bankroll, wins, losses, games_played):
    bet = take_bet()

    """ User Selectis 4 common roulette bet types:"""
    roulette_game = input("Select your bet type: 1 - Red/Black/Green, 2 - Odd/Even, 3 - Dozens (1-12 / 13-24 / 25-36), 4 - Specific Number: ")

    roulette_spin = random.randint(0, 36)  # 0 is green, 1-36 are red or black

    ## 1. Red / Black / Green Game
    if roulette_game == "1":
        color_choice = input("Choose Red, Black, or Green: ")

        if color_choice not in ["Red", "Black", "Green"]:
            print("Invalid color choice. Please try again.")
            return bankroll, wins, losses, games_played
        
        # simple for loop animation
        for i in range(3):
            print("Spinning...")
            time.sleep(0.8)

        # Results
        if roulette_spin == 0:          # 0 is green
            result = "Green"
        elif roulette_spin % 2 == 0:    # even numbers are red, odd numbers are black
            result = "Red"
        else:
            result = "Black"

        print("The roulette spin result is:", roulette_spin, result)    # displays result

        games_played += 1

        if color_choice == result:
            if result == "Green":
                print("You hit green, huge win!")
                bankroll += bet * 35    # 35:1 payout for green
                wins += 1
            else:
                print("You win!")
                bankroll += bet # 1:1 payout for red or black
                wins += 1
        else:
            print("You lose!")
            bankroll -= bet
            losses += 1

    ## 2. Odd / Even Game
    elif roulette_game == "2":
        odd_even_choice = input("Choose Odd or Even: ")

        if odd_even_choice not in ["Odd", "Even"]:
            print("Invalid choice. Please try again.")
            return bankroll, wins, losses, games_played

        # simple for loop animation
        for i in range(3):
            print("Spinning...")
            time.sleep(0.8)

        # Results
        if roulette_spin == 0:          # 0 is neither odd nor even
            result = "Neither"
        elif roulette_spin % 2 == 0:    # even numbers are even, odd numbers are odd
            result = "Even"
        else:
            result = "Odd"

        print("The roulette spin result is:", roulette_spin, result)

        games_played += 1

        if odd_even_choice == result:
            print("You win!")
            bankroll += bet # 1:1 payout for odd or even
            wins += 1
        else:
            print("You lose!")
            bankroll -= bet
            losses += 1

    ## 3. Dozens
    elif roulette_game == "3":
        dozen_choice = input("Choose a dozen: 1 - (1-12), 2 - (13-24), 3 - (25-36): ")

        if dozen_choice not in ["1", "2", "3"]:
            print("Invalid dozen choice. Please try again.")
            return bankroll, wins, losses, games_played

        # simple for loop animation
        for i in range(3):
            print("Spinning...")
            time.sleep(0.8)

        # Results
        print("The roulette spin result is:", roulette_spin)

        games_played += 1

        if roulette_spin == 0:          # 0 is not included in any dozen (house edge)
            print("0 is not in any dozen.")
            print("You lose!")
            bankroll -= bet
            losses += 1

        elif dozen_choice == "1" and 1 <= roulette_spin <= 12:
            print("You win!")
            bankroll += bet * 2         # 2:1 payout for dozens bet
            wins += 1

        elif dozen_choice == "2" and 13 <= roulette_spin <= 24:
            print("You win!")
            bankroll += bet * 2         # 2:1 payout for dozens bet
            wins += 1

        elif dozen_choice == "3" and 25 <= roulette_spin <= 36:
            print("You win!")
            bankroll += bet * 2         # 2:1 payout for dozens bet
            wins += 1

        else:
            print("You lose!")
            bankroll -= bet #lose the bet amount
            losses += 1

    ## 4. Specific Number
    elif roulette_game == "4":
        number_choice = int(input("Choose a number to bet on (0-36): "))

        if number_choice < 0 or number_choice > 36:
            print("Invalid number choice. Please try again.")
            return bankroll, wins, losses, games_played

        # simple for loop animation
        for i in range(3):
            print("Spinning...")
            time.sleep(0.8)

        # Results
        print("The roulette spin result is:", roulette_spin)

        games_played += 1

        if number_choice == roulette_spin:
            print("You win!")
            bankroll += bet * 35    # 35:1 payout for guessing the specific number on the roulette wheel
            wins += 1
        else:
            print("You lose!")
            bankroll -= bet
            losses += 1

    else:
        print("Invalid roulette game choice.")

    return bankroll, wins, losses, games_played


while True:
    print("Your current bankroll is: $", bankroll)

## Menu, user input for which game to play and how much to bet

    print("Choose a game:")
    print("1 - Coin Flip")
    print("2 - Dice Roll")
    print("3 - Roulette")
    print("4 - Blackjack")
    print("5 - Betting Odds")
    print("6 - Stats")
    print("7 - Quit")

    game_choice = input("Enter the number of the game you want to play: ")

## 1. Coin Flip 
    if game_choice == "1":
        bankroll, wins, losses, games_played = play_coin_flip(bankroll, wins, losses, games_played)

## 2. Dice Game

    elif game_choice == "2":
        bankroll, wins, losses, games_played = play_dice_game(bankroll, wins, losses, games_played)

## 3. Roulette
    elif game_choice == "3":
        bankroll, wins, losses, games_played = play_roulette(bankroll, wins, losses, games_played)

## 4. Blackjack
    elif game_choice == "4":
        print("Blackjack game coming soon!")
        continue

## 5. Betting Odds

    elif game_choice == "5":
        print("Betting odds:")
        print("Coin Flip: 1:1 payout. 50% heads, 50% tails")
        print("Dice Game - Over/Under: 1:1 payout. 50% over 3.5, 50% under 3.5")
        print("Dice Game - Exact Number: 5:1 payout. 16.67% chance to guess the exact number on a 6 sided die")
        print("Roulette - Red/Black: 1:1 payout. 18/38 chance to hit red or black on a standard roulette wheel")
        print("Roulette - Green: 35:1 payout. 2/38 chance to hit green on a standard roulette wheel")
        print("Roulette - Odd/Even: 1:1 payout. 18/38 chance to hit odd or even on a standard roulette wheel")

        input("\nPress Enter to return to the menu...") 
        continue

## 6. Stats (previous bets and outcomes, current bankroll)

    elif game_choice == "6":
        print("Your current bankroll is: $", bankroll)
        print("Games played:", games_played)
        print("Wins:", wins)
        print("Losses:", losses)
        print("Profit/Loss: $", bankroll - 1000) # calculates profit or loss based on starting bankroll of $1000

        if games_played > 0:
            win_rate = (wins / games_played) * 100
            print("Win rate:", round(win_rate, 2), "%")
        else:
            print("Win rate: 0.0 %")

        input("\nPress Enter to return to the menu...")
        continue

## 7. Quit
    elif game_choice == "7":
        print("Thanks for playing! Your final bankroll is: $", bankroll)
        break

## wrong input for game select

    else:
        print("Invalid choice, please try again")
        continue

## Balance check
    if bankroll <= 0:
        print("You are out of money! Game over.")
        break

    again = input("Do you want to continue? (y/n) ")
    if again == "n":
        break

    