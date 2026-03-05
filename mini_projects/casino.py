import random

# Bankroll = cash the player has to bet with
bankroll = 1000


## function to take bet
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

### taking bet
        bet = take_bet()

# Game starts
        """ take user input for heads or tails"""
        choice = input("Choose heads or tails: ")
        if choice not in ["heads", "tails"]:
            print("Invalid choice. Please try again.")
            continue

        coin_flip = random.randint(0, 1) # 0 for heads, 1 for tails


        if coin_flip == 0:
            result = "heads"
        else:
            result = "tails"
        print("The coin flip result is: ", result)

        if choice == result:
            print("You win!")
            bankroll += bet # 1:1 payout for coin flip
        else:
            print("You lose!")
            bankroll -= bet # lose the bet amount
    
    

## 2. Dice Game

    elif game_choice == "2":

### taking bet

        bet = take_bet()
        dice_game = input("Select your bet type: 1 - Over/Under, 2 - Exact Number: ")

# 2.1 Guess over or under 3.5, payout is 1:1 for guessing correctly if dice roll is over or under 3.5

        if dice_game == "1":

            """number_of_dice = int(input("How many dice do you want to roll? (1-3): "))
            if number_of_dice < 1 or number_of_dice > 3:    # make sure player can only roll 1-3 dice to avoid large rolls and payouts
                print("Invalid number of dice. Please try again.")
                continue
            for i in range(number_of_dice): # roll the dice for the number of dice the player wants to play with, we can sum the rolls to get a total roll for over/under bet
                dice_roll = random.randint(1, 6) # roll a 6 sided dice for each die"""
            
            dice_roll = random.randint(1, 6) # roll a single 6 sided die for over/under bet

            # game start    
            guess = input("Do you think the dice roll will be over or under 3.5? (over/under): ")
            if guess not in ["over", "under"]:
                print("Invalid choice. Please try again.")
                continue

            print("The dice roll result is: ", dice_roll)

            if (guess == "over" and dice_roll > 3.5) or (guess == "under" and dice_roll < 3.5): # > 3.5 means 4, 5, or 6 and < 3.5 means 1, 2, or 3
                print("You win!")
                bankroll += bet # 1:1 payout for guessing over or under correctly
            else:
                print("You lose!")
                bankroll -= bet # lose the bet amount

# 2.2 Guess the exact number on the dice, payout is 5:1 for guessing the exact number in dice

        elif dice_game == "2":

            guess = int(input("Guess the dice roll (1-6): "))
            dice_roll = random.randint(1, 6)

            print("The dice roll result is: ", dice_roll)

            if guess == dice_roll:
                print("You win!")
                bankroll += bet * 5 # 5:1 payout for guessing the exact number in dice

            else:
                print("You lose!")
                bankroll -= bet # lose the bet amount



## 3. Roulette
    elif game_choice == "3":

### taking bet

        bet = take_bet()

# game starts
        roulette_game = input("Select your bet type: 1 - Red/Black/Green, 2 - Odd/Even, 3 - Specific Number: ")
        roulette_spin = random.randint(0, 36) # 0 is green, 1-36 are red or black

        ## 3.1 Red/Black/Green Roulette Bet

        if roulette_game == "1":
            color_choice = input("Choose Red, Black, or Green: ")

            if color_choice not in ["Red", "Black", "Green"]:
                print("Invalid color choice. Please try again.")
                continue

            if roulette_spin == 0:
                result = "Green"
            elif roulette_spin % 2 == 0:
                result = "Red"
            else:
                result = "Black"

            print("The roulette spin result is: ", roulette_spin, result)

            if color_choice == result:
                if result == "Green":
                    print("You hit green, huge win!")
                    bankroll += bet * 35 # 35:1 payout for green
                else:
                    print("You win!")
                    bankroll += bet # 1:1 payout for red or black
            else:
                print("You lose!")
                bankroll -= bet # lose the bet amount
     
        ## 3.2 Odd/Even Roulette Bet
        elif roulette_game == "2":

            odd_even_choice = input("Choose Odd or Even: ")
            if odd_even_choice not in ["Odd", "Even"]:
                print("Invalid choice. Please try again.")
                continue

            if roulette_spin == 0:
                result = "Neither"
            elif roulette_spin % 2 == 0:
                result = "Even"
            else:
                result = "Odd"

            print("The roulette spin result is: ", result)

            if odd_even_choice == result:
                print("You win!")
                bankroll += bet # 1:1 payout for odd or even
            else:
                print("You lose!")
                bankroll -= bet # lose the bet amount

        ## 3.3 Specific Number Roulette Bet
        elif roulette_game == "3":

            number_choice = int(input("Choose a number to bet on (0-36): "))

            if number_choice < 0 or number_choice > 36:
                print("Invalid number choice. Please try again.")
                continue

            print("The roulette spin result is: ", roulette_spin)

            if number_choice == roulette_spin:
                print("You win!")
                bankroll += bet * 35 # 35:1 payout for specific number
            else:
                print("You lose!")
                bankroll -= bet # lose the bet amount

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
        continue

## 6. Stats (previous bets and outcomes, current bankroll)

    elif game_choice == "6":
        print("Your current bankroll is: $", bankroll)
        print("Stats feature coming soon")
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

    