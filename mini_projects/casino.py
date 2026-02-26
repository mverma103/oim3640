import random

# Bankroll = cash the player has to bet with
bankroll = 1000

while True:
    print("Your current bankroll is: $", bankroll)

## Menu, user input for which game to play and how much to bet

    print("Choose a game:")
    print("1 - Coin Flip")
    print("2 - Dice Roll")
    print("3 - Roulette")
    print("4 - Blackjack (coming soon)")
    print("5 - Betting Odds")
    print("6 - Stats")

    game_choice = input("Enter the number of the game you want to play: ")
    


## Coin Flip
    if game_choice == "1":

### taking bet
        bet = int(input("How much do you want to bet?"))
        if bet < 50: # make a $50 minimum bet to avoid loop of small bets
            print("Minimum bet is $50. Please try again.")
            continue
        elif bet > bankroll: # make sure player cannot bet more than they have
            print("You cannot bet more than your current bankroll. Please try again.")
            continue
        elif bet % 50 != 0: # make sure bet is in increments of $50 to avoid small bets
            print("Bet must be in increments of $50. Please try again.")
            continue

# Game starts
        choice = input("Choose heads or tails: ")
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
    
    

## Dice Game

    elif game_choice == "2":

### taking bet
        bet = int(input("How much do you want to bet?"))
        if bet < 50: # make a $50 minimum bet to avoid loop of small bets
            print("Minimum bet is $50. Please try again.")
            continue
        elif bet > bankroll: # make sure player cannot bet more than they have
            print("You cannot bet more than your current bankroll. Please try again.")
            continue
        elif bet % 50 != 0: # make sure bet is in increments of $50 to avoid small bets
            print("Bet must be in increments of $50. Please try again.")
            continue

# game starts
        guess = int(input("Guess the dice roll (1-6): "))
        dice_roll = random.randint(1, 6)

        print("The dice roll result is: ", dice_roll)

        if guess == dice_roll:
            print("You win!")
            bankroll += bet * 5 # 5:1 payout for guessing the exact number in dice

        else:
            print("You lose!")
            bankroll -= bet # lose the bet amount

## Roulette
    elif game_choice == "3":

### taking bet

        bet = int(input("How much do you want to bet?"))
        if bet < 50: # make a $50 minimum bet to avoid loop of small bets
            print("Minimum bet is $50. Please try again.")
            continue
        elif bet > bankroll: # make sure player cannot bet more than they have
            print("You cannot bet more than your current bankroll. Please try again.")
            continue
        elif bet % 50 != 0: # make sure bet is in increments of $50 to avoid small bets
            print("Bet must be in increments of $50. Please try again.")
            continue

# game starts
        roulette_game = input("Select your bet type: 1 - Red/Black/Green, 2 - Odd/Even, 3 - Specific Number: ")
        roulette_spin = random.randint(0, 36) # 0 is green, 1-36 are red or black

## Red/Black/Green Roulette Bet

        if roulette_game == "1":
            color_choice = input("Choose Red, Black, or Green: ")

            if roulette_spin == 0:
                result = "Green"
            elif roulette_spin % 2 == 0:
                result = "Red"
            else:
                result = "Black"

            print("The roulette spin result is: ", result)

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
     
# Odd/Even Roulette Bet
        elif roulette_game == "2":

            odd_even_choice = input("Choose Odd or Even: ")

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













## wrong input for game select

    else:
        print("Invalid choice, please try again")
        continue

## Balance check
    if bankroll <= 0:
        print("You are out of money! Game over.")
        break

    again = input("Do you want to play again? (y/n) ")
    if again == "n":
        break

    