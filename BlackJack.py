import random
from enum import Enum, auto
from tqdm import tqdm

class PlayOptions(Enum):
    STAY = 1
    HIT = 2
    DOUBLE = 3
    SURRENDER = 5
    SPLIT = 4

class DealerResults(Enum):
    BLACKJACK = 1
    BUSTED = 2
    STAY = 3

class HandType(Enum):
    NORMAL = 1
    SPLIT = 2
    DOUBLE = 3

class HandResults(Enum):
    WIN = auto()
    DOUBLEWIN = auto()
    DOUBLELOSS = auto()
    BLACKJACK = auto()
    LOST = auto()
    PUSH = auto()
    SURRENDER = auto()

hardHand2CardLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT],
    [PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],  # replaced surrender
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],  # replaced surrender
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

hardHandLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

softHand2CardLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

softHandLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

pairHandLookup = [
    # Replaced any 'SURRENDER' with e.g. HIT
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT],
    [PlayOptions.STAY, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.STAY, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

###########################################################
# Single-deck Shoe with insurance threshold at TC>=3, etc. #
###########################################################
class Shoe:
    def __init__(self, num_decks=1):
        self.decks = num_decks
        self.cards = []
        for i in range(52 * self.decks):
            raw_rank = (i % 52) % 13 + 1
            # Convert face cards to 10
            self.cards.append(10 if raw_rank > 10 else raw_rank)
        self.running_count = 0

    def shuffle(self):
        self.__init__(self.decks)

    def cardsRemaining(self):
        return len(self.cards)

    def getTrueCount(self):
        decks_left = max(0.01, self.cardsRemaining() / 52.0)
        return self.running_count / decks_left

    def getBet(self):
        tc = self.getTrueCount()
        if tc < 1:
            return 1
        elif tc < 3:
            return 3
        elif tc < 6:
            return 5
        else:
            return 10

    def getCard(self):
        if not self.cards:
            self.shuffle()
        card = random.choice(self.cards)
        self.cards.remove(card)
        # Hi-lo adjust
        if card in [2, 3, 4, 5, 6]:
            self.running_count += 1
        elif card in [1, 10]:
            self.running_count -= 1
        return card

######################################################
# Hand class: no surrender, but we do allow insurance #
######################################################
class Hand:
    def __init__(self):
        self.cards = []
        self.handType = HandType.NORMAL
        self.result = None

    def addCard(self, card):
        self.cards.append(card)

    def getHandTotal(self):
        total = 0
        aces_as_11 = 0
        for c in self.cards:
            if c == 1:
                total += 11
                aces_as_11 += 1
            else:
                total += c
        while total > 21 and aces_as_11 > 0:
            total -= 10
            aces_as_11 -= 1
        return total

    def isSoftHand(self):
        total = 0
        aces_as_11 = 0
        for c in self.cards:
            if c == 1:
                total += 11
                aces_as_11 += 1
            else:
                total += c
        while total > 21 and aces_as_11 > 0:
            total -= 10
            aces_as_11 -= 1
        return (aces_as_11 > 0 and total <= 21)

    def isBlackJack(self):
        return (len(self.cards) == 2) and (self.getHandTotal() == 21)

    def dealerPlay(self):
        total = self.getHandTotal()
        soft = self.isSoftHand()
        if len(self.cards) == 2 and total == 21:
            return PlayOptions.STAY
        if total < 17 or (total == 17 and soft):
            return PlayOptions.HIT
        return PlayOptions.STAY

    def basicStrategyPlay(self, dealerFaceCard, trueCount=0):
        handTotal = self.getHandTotal()
        softHand = self.isSoftHand()

        if len(self.cards) < 2:
            return PlayOptions.HIT
        if handTotal > 21:
            return PlayOptions.STAY

        # Basic Strategy
        if len(self.cards) == 2:
            if self.cards[0] == self.cards[1]:
                action = pairHandLookup[self.cards[0] - 1][dealerFaceCard - 1]
            elif softHand:
                action = softHand2CardLookup[handTotal - 13][dealerFaceCard - 1]
            else:
                action = hardHand2CardLookup[handTotal - 5][dealerFaceCard - 1]
        else:
            if softHand:
                action = softHandLookup[handTotal - 13][dealerFaceCard - 1]
            else:
                action = hardHandLookup[handTotal - 5][dealerFaceCard - 1]

        # Deviations
        # Split 10s vs 5 if TC≥5 or vs 6 if TC≥6
        if len(self.cards) == 2 and self.cards[0] == 10 and self.cards[1] == 10:
            if dealerFaceCard == 5 and trueCount >= 5:
                action = PlayOptions.SPLIT
            elif dealerFaceCard == 6 and trueCount >= 6:
                action = PlayOptions.SPLIT

        # Stand on 16 vs T if TC>0
        if handTotal == 16 and dealerFaceCard == 10 and trueCount > 0:
            action = PlayOptions.STAY

        # Stand on 15 vs T if TC≥4
        if handTotal == 15 and dealerFaceCard == 10 and trueCount >= 4:
            action = PlayOptions.STAY

        return action

#################################################
# Player, Dealer, & Table classes with INSURANCE #
#################################################
class Player:
    def __init__(self):
        self.hands = [Hand()]

class Dealer:
    def __init__(self):
        self.hand = Hand()

class Table:
    def __init__(self):
        self.shoe = Shoe(1)
        self.player = Player()
        self.dealer = Dealer()
        self.activeHands = 1
        self.insurance_bet = 0.0
        self.profit_from_round = 0.0

    def dealFirstTwoCards(self):
        for _ in range(2):
            self.player.hands[0].addCard(self.shoe.getCard())
            self.dealer.hand.addCard(self.shoe.getCard())

    def offerInsurance(self, bet):
        # If dealer upcard = Ace & True Count >= 3 => buy insurance
        if self.dealer.hand.cards[1] == 1 and self.shoe.getTrueCount() >= 3:
            self.insurance_bet = bet / 2.0
        else:
            self.insurance_bet = 0.0

    def playRound(self):
        # Bet based on current true count
        bet = self.shoe.getBet()
        self.profit_from_round = 0

        # Check if there are enough cards to deal a hand
        if self.shoe.cardsRemaining() < 6:
            self.shoe.shuffle()
            return None  # Indicate that the hand was voided

        # Reset hands
        self.player.hands = [Hand()]
        self.dealer.hand = Hand()

        self.dealFirstTwoCards()

        # If dealer doesn't have blackjack, player acts
        if not self.dealer.hand.isBlackJack():
            self.playPlayerHand(self.player.hands[0], self.dealer.hand.cards[0])
            # Dealer action if player isn't already out
            if self.activeHands > 0:
                while True:
                    dealer_action = self.dealer.hand.dealerPlay()
                    if dealer_action == PlayOptions.STAY:
                        break
                    elif dealer_action == PlayOptions.HIT:
                        if self.shoe.cardsRemaining() == 0:
                            self.shoe.shuffle()
                            return None  # Indicate that the hand was voided
                        self.dealer.hand.addCard(self.shoe.getCard())

        # Resolve
        self.recordHandResults(bet)
        return self.profit_from_round

    def playPlayerHand(self, hand, dealer_upcard):
        self.activeHands = 1
        if hand.isBlackJack():
            self.activeHands -= 1
            return

        while True:
            tc = self.shoe.getTrueCount()
            move = hand.basicStrategyPlay(dealer_upcard, tc)

            if move in [PlayOptions.HIT, PlayOptions.DOUBLE]:
                hand.addCard(self.shoe.getCard())
            elif move == PlayOptions.SPLIT:
                # Not implementing advanced splitting logic here
                break

            if move in [PlayOptions.STAY, PlayOptions.DOUBLE]:
                break

        # Check bust on final
        if hand.getHandTotal() > 21:
            self.activeHands -= 1
            if hand.handType == HandType.DOUBLE:
                hand.result = HandResults.DOUBLELOSS
            else:
                hand.result = HandResults.LOST
        elif move == PlayOptions.DOUBLE:
            hand.handType = HandType.DOUBLE

    def recordHandResults(self, bet):
        ph = self.player.hands[0]
        if ph.result is not None:
            # Already decided (bust, etc.)
            if ph.result == HandResults.LOST:
                self.profit_from_round -= bet
            elif ph.result == HandResults.DOUBLELOSS:
                self.profit_from_round -= (2 * bet)
            return

        dealer_total = self.dealer.hand.getHandTotal()
        player_total = ph.getHandTotal()

        if dealer_total > 21:
            # Dealer bust
            if ph.handType == HandType.DOUBLE:
                self.profit_from_round += (2 * bet)
            else:
                self.profit_from_round += bet
        else:
            if player_total == dealer_total:
                # push
                pass
            elif player_total > dealer_total:
                if ph.handType == HandType.DOUBLE:
                    self.profit_from_round += (2 * bet)
                else:
                    self.profit_from_round += bet
            else:
                # dealer wins
                if ph.handType == HandType.DOUBLE:
                    self.profit_from_round -= (2 * bet)
                else:
                    self.profit_from_round -= bet

        # Check if player had a blackjack => +0.5 * bet on top of normal win
        if ph.isBlackJack() and ph.handType == HandType.NORMAL:
            # Means dealer didn't have BJ => 3:2 payoff => +0.5
            self.profit_from_round += (0.5 * bet)

###############################################
# Extended Simulation with True Count Tracking #
###############################################
def simulate_blackjack(number_of_shoes=10000):
    table = Table()
    total_profit = 0.0
    true_count_changes = []
    highest_true_counts = []
    lowest_true_counts = []
    total_hands = 0
    total_blackjacks = 0

    overall_max_true_count = float('-inf')
    overall_min_true_count = float('inf')
    cards_at_max_true_count = []
    cards_at_min_true_count = []

    # Add a progress bar to the simulation loop
    for _shoe_idx in tqdm(range(number_of_shoes), desc="Simulating Blackjack"):
        shoe_profit = 0.0
        initial_true_count = table.shoe.getTrueCount()
        max_true_count = initial_true_count
        min_true_count = initial_true_count
        cards_at_max_this_shoe = table.shoe.cards[:]
        cards_at_min_this_shoe = table.shoe.cards[:]
        hands_this_shoe = 0
        blackjacks_this_shoe = 0

        # Keep dealing rounds until <20 cards remain (provides buffer for hits)
        while table.shoe.cardsRemaining() >= 20:
            # Track true count changes before playing a round
            current_true_count = table.shoe.getTrueCount()
            if current_true_count > max_true_count:
                max_true_count = current_true_count
                cards_at_max_this_shoe = table.shoe.cards[:]
            if current_true_count < min_true_count:
                min_true_count = current_true_count
                cards_at_min_this_shoe = table.shoe.cards[:]

            round_profit = table.playRound()
            shoe_profit += round_profit
            hands_this_shoe += 1
            if table.player.hands[0].isBlackJack():
                blackjacks_this_shoe += 1

        # Update overall max and min true counts and their corresponding cards
        if max_true_count > overall_max_true_count:
            overall_max_true_count = max_true_count
            cards_at_max_true_count = cards_at_max_this_shoe
        if min_true_count < overall_min_true_count:
            overall_min_true_count = min_true_count
            cards_at_min_true_count = cards_at_min_this_shoe

        # Store max and min true counts for this shoe
        highest_true_counts.append(max_true_count)
        lowest_true_counts.append(min_true_count)
        total_hands += hands_this_shoe
        total_blackjacks += blackjacks_this_shoe

        # Once <20 cards, that shoe is done. Shuffle for next shoe.
        table.shoe.shuffle()
        total_profit += shoe_profit

    # Calculate statistics
    average_highest_true_count = sum(highest_true_counts) / len(highest_true_counts)
    average_lowest_true_count = sum(lowest_true_counts) / len(lowest_true_counts)
    average_ev_per_shoe = total_profit / number_of_shoes
    average_hands_per_shoe = total_hands / number_of_shoes
    average_blackjacks_per_shoe = total_blackjacks / number_of_shoes

    print(f"Simulation Results:")
    print(f"-------------------")
    print(f"Highest true count seen: {overall_max_true_count}")
    print(f"Lowest true count seen: {overall_min_true_count}")
    print(f"Average highest true count per shoe: {average_highest_true_count:.2f}")
    print(f"Average lowest true count per shoe: {average_lowest_true_count:.2f}")
    print(f"Average EV per shoe: {average_ev_per_shoe:.2f}")
    print(f"Average hands per shoe: {average_hands_per_shoe:.2f}")
    print(f"Average player blackjacks per shoe: {average_blackjacks_per_shoe:.2f}")
    print(f"Cards left in the shoe at highest true count: {cards_at_max_true_count}")
    print(f"Cards left in the shoe at lowest true count: {cards_at_min_true_count}")

if __name__ == "__main__":
    simulate_blackjack(500000)