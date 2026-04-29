import random

# number of decks used in the blackjack game
NUM_DECKS = 4

# deck of cards, each face card = 10, ace = 11
def create_deck():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = cards * 4 * NUM_DECKS
    random.shuffle(deck)
    return deck

# function to deal a card from the deck
def deal_card(deck):
    return deck.pop()

# function to calculate the total value of a hand, accounting for aces
def calculate_hand(hand):
    total = sum(hand)

    # adjust for aces if total is over 21
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)

    return total

# function to display a hand and its total
def show_hand(name, hand):
    print(name, "hand:", hand)
    print(name, "total:", calculate_hand(hand))


# function to check if the hand is soft, meaning it has an ace counted as 11 (to help with strategy_hint)
def is_soft_hand(hand):
    if 11 in hand and sum(hand) <= 21:
        return True
    else:
        return False


# function to give a detailed blackjack basic strategy hint
def strategy_hint(player_hand, dealer_card):
    player_total = calculate_hand(player_hand)

    # pair strategy, used when first two cards are the same
    if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
        pair_card = player_hand[0]

        if pair_card == 11:
            return "Hint: Split Aces."

        elif pair_card == 8:
            return "Hint: Split 8s."

        elif pair_card == 10:
            return "Hint: Stand. Do not split 10s."

        elif pair_card == 9:
            if dealer_card in [2, 3, 4, 5, 6, 8, 9]:
                return "Hint: Split 9s."
            else:
                return "Hint: Stand."

        elif pair_card == 7:
            if dealer_card in [2, 3, 4, 5, 6, 7]:
                return "Hint: Split 7s."
            else:
                return "Hint: Hit."

        elif pair_card == 6:
            if dealer_card in [2, 3, 4, 5, 6]:
                return "Hint: Split 6s."
            else:
                return "Hint: Hit."

        elif pair_card == 5:
            if dealer_card in [2, 3, 4, 5, 6, 7, 8, 9]:
                return "Hint: Double down."
            else:
                return "Hint: Hit."

        elif pair_card == 4:
            if dealer_card in [5, 6]:
                return "Hint: Split 4s."
            else:
                return "Hint: Hit."

        elif pair_card == 3 or pair_card == 2:
            if dealer_card in [2, 3, 4, 5, 6, 7]:
                return "Hint: Split."
            else:
                return "Hint: Hit."

    # soft hand strategy, used when player has an ace counted as 11
    if is_soft_hand(player_hand):
        if player_total <= 17:
            if dealer_card in [5, 6]:
                return "Hint: Double down if allowed, otherwise hit."
            else:
                return "Hint: Hit."

        elif player_total == 18:
            if dealer_card in [2, 3, 4, 5, 6]:
                return "Hint: Double down if allowed, otherwise stand."
            elif dealer_card in [7, 8]:
                return "Hint: Stand."
            else:
                return "Hint: Hit."

        elif player_total >= 19:
            return "Hint: Stand."

    # hard hand strategy, used when there is no ace counted as 11
    if player_total <= 8:
        return "Hint: Hit."

    elif player_total == 9:
        if dealer_card in [3, 4, 5, 6]:
            return "Hint: Double down if allowed, otherwise hit."
        else:
            return "Hint: Hit."

    elif player_total == 10:
        if dealer_card in [2, 3, 4, 5, 6, 7, 8, 9]:
            return "Hint: Double down if allowed, otherwise hit."
        else:
            return "Hint: Hit."

    elif player_total == 11:
        return "Hint: Double down if allowed, otherwise hit."

    elif player_total == 12:
        if dealer_card in [4, 5, 6]:
            return "Hint: Stand."
        else:
            return "Hint: Hit."

    elif player_total in [13, 14, 15, 16]:
        if dealer_card in [2, 3, 4, 5, 6]:
            return "Hint: Stand."
        else:
            return "Hint: Hit."

    elif player_total >= 17:
        return "Hint: Stand."

    return "Hint: Use your judgment."


# function to get the player's bet
def get_bet(bankroll):
    while True:
        bet = int(input("Enter your bet: $"))

        if bet <= 4:
            print("Minimum bet is $5.")
        elif bet > bankroll:
            print("You cannot bet more than your bankroll.")
        else:
            return bet

# player's turn to hit, stand, or double down
def player_turn(deck, player_hand, bankroll, bet, dealer_card):
    while calculate_hand(player_hand) < 21:
        show_hand("Player", player_hand)

        see_hint = input("Do you want a hint? (yes/no): ").lower()

        if see_hint == "yes":
            print("\n--- STRATEGY ---")
            print(strategy_hint(player_hand, dealer_card))
            print("----------------\n")

        choice = input("Do you want to hit, stand, or double? ").lower()

        if choice == "hit":
            player_hand.append(deal_card(deck))

        elif choice == "stand":
            break

        elif choice == "double":
            if bankroll >= bet * 2:
                bet = bet * 2
                player_hand.append(deal_card(deck))
                print("You doubled down.")
                show_hand("Player", player_hand)
                break
            else:
                print("You do not have enough money to double down.")

        else:
            print("Please type hit, stand, or double.")

    return bet

# dealer hit until total is 17 or higher
def dealer_turn(deck, dealer_hand):
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

# function to settle the bet and return how much the bankroll should change
def settle_bet(player_hand, dealer_hand, bet):
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    print("\nFinal Results:")
    show_hand("Player", player_hand)
    show_hand("Dealer", dealer_hand)

    if player_total > 21:
        print("You busted. You lose $", bet)
        return -bet, "loss"

    elif dealer_total > 21:
        print("Dealer busted. You win $", bet)
        return bet, "win"

    elif player_total == 21 and len(player_hand) == 2:
        blackjack_win = bet * 1.5
        print("Blackjack! You win $", blackjack_win)
        return blackjack_win, "win"

    elif player_total > dealer_total:
        print("You win $", bet)
        return bet, "win"

    elif dealer_total > player_total:
        print("Dealer wins. You lose $", bet)
        return -bet, "loss"

    else:
        print("Push. Your bet is returned.")
        return 0, "push"

# function to check if the player can split their hand (AI assisted me)
def can_split(player_hand, bankroll, bet):
    if len(player_hand) == 2 and player_hand[0] == player_hand[1] and bankroll >= bet * 2:
        return True
    else:
        return False

# function to play both split hands
def play_split_hands(deck, player_hand, dealer_hand, bankroll, bet, stats):
    hand1 = [player_hand[0], deal_card(deck)]
    hand2 = [player_hand[1], deal_card(deck)]

    total_change = 0

    print("\n--- Playing Split Hand 1 ---")
    final_bet1 = player_turn(deck, hand1, bankroll, bet, dealer_hand[0])

    print("\n--- Playing Split Hand 2 ---")
    final_bet2 = player_turn(deck, hand2, bankroll, bet, dealer_hand[0])

    dealer_turn(deck, dealer_hand)

    print("\n--- Result for Hand 1 ---")
    change1, result_type1 = settle_bet(hand1, dealer_hand, final_bet1)
    total_change += change1
    stats[result_type1] += 1

    print("\n--- Result for Hand 2 ---")
    change2, result_type2 = settle_bet(hand2, dealer_hand, final_bet2)
    total_change += change2
    stats[result_type2] += 1

    return total_change

# function to play one round of blackjack
def play_round(deck, bankroll, stats):
    print("\nBankroll: $", bankroll)

    bet = get_bet(bankroll)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print("\nDealer is showing:", dealer_hand[0])
    show_hand("Player", player_hand)

    # ask the player if they want to split if they have two matching cards
    if can_split(player_hand, bankroll, bet):
        split_choice = input("You can split. Do you want to split? yes/no: ").lower()

        if split_choice == "yes":
            result = play_split_hands(deck, player_hand, dealer_hand, bankroll, bet, stats)
            bankroll += result
            return bankroll

    final_bet = player_turn(deck, player_hand, bankroll, bet, dealer_hand[0])

    if calculate_hand(player_hand) <= 21:
        dealer_turn(deck, dealer_hand)

    change, result_type = settle_bet(player_hand, dealer_hand, final_bet)
    bankroll += change
    stats[result_type] += 1

    return bankroll

""" MONTE CARLO SIMULATION: """

# automatic player strategy for simulation
def simulation_player_turn(deck, player_hand, dealer_card):
    while calculate_hand(player_hand) < 17:
        player_hand.append(deal_card(deck))


# function to run many blackjack hands automatically
def run_simulation(num_rounds):
    wins = 0
    losses = 0
    pushes = 0

    for i in range(num_rounds):
        deck = create_deck()

        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        simulation_player_turn(deck, player_hand, dealer_hand[0])

        if calculate_hand(player_hand) <= 21:
            dealer_turn(deck, dealer_hand)

        player_total = calculate_hand(player_hand)
        dealer_total = calculate_hand(dealer_hand)

        if player_total > 21:
            losses += 1
        elif dealer_total > 21:
            wins += 1
        elif player_total > dealer_total:
            wins += 1
        elif dealer_total > player_total:
            losses += 1
        else:
            pushes += 1

    print("\n--- Monte Carlo Simulation Results ---")
    print("Rounds simulated:", num_rounds)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Pushes:", pushes)
    print("Win rate:", round(wins / num_rounds * 100, 2), "%")


""" UI FUNCTIONS """

# function to print a divider for cleaner terminal output
def print_divider():
    print("\n" + "=" * 45)


# function to print the main title
def print_title():
    print_divider()
    print("♠️  ♥️  WELCOME TO BLACKJACK  ♦️  ♣️")
    print_divider()


# function to show the menu
def show_menu():
    print("\nMenu:")
    print("1. Play Blackjack")
    print("2. Run Monte Carlo Simulation")
    print("3. View Stats")
    print("4. Quit")



# function to show stats from the actual game
def show_stats(stats, bankroll):
    print_divider()
    print("GAME STATS")
    print_divider()
    print("Wins:", stats["win"])
    print("Losses:", stats["loss"])
    print("Pushes:", stats["push"])
    print("Current bankroll: $", bankroll)


# main function to run the blackjack game
def main():
    print_title()
    print("This table uses", NUM_DECKS, "decks.")

    bankroll = 100
    deck = create_deck()

    stats = {
        "win": 0,
        "loss": 0,
        "push": 0
    }

    while bankroll > 0:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            if len(deck) < 20:
                print("\nDeck is running low. Reshuffling...")
                deck = create_deck()

            bankroll = play_round(deck, bankroll, stats)

        elif choice == "2":
            rounds = int(input("How many rounds should the simulation run? "))
            run_simulation(rounds)

        elif choice == "3":
            show_stats(stats, bankroll)

        elif choice == "4":
            break

        else:
            print("Please choose 1, 2, 3, or 4.")

    print("\nThanks for playing!")

main()