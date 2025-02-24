import random
from enum import Enum, auto
from tqdm import tqdm
import Strategy

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

###########################################################
# Single-deck Shoe with insurance threshold at TC>=3, etc. #
###########################################################
class Shoe:
    def __init__(self, num_decks=1):
        self.decks = num_decks
        self.cards = []
        for i in range(52 * self.decks):
            raw_rank = (i % 52) % 13 + 1
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
        return Strategy.getBet(self.getTrueCount())

    def getCard(self):
        if not self.cards:
            self.shuffle()
        card = random.choice(self.cards)
        self.cards.remove(card)
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
            return Strategy.PlayOptions.STAY
        if total < 17 or (total == 17 and soft):
            return Strategy.PlayOptions.HIT
        return Strategy.PlayOptions.STAY

    def basicStrategyPlay(self, dealerFaceCard, trueCount=0):
        handTotal = self.getHandTotal()
        softHand = self.isSoftHand()

        if len(self.cards) < 2:
            return Strategy.PlayOptions.HIT
        if handTotal > 21:
            return Strategy.PlayOptions.STAY

        if len(self.cards) == 2:
            if self.cards[0] == self.cards[1]:
                action = Strategy.pairHandLookup[self.cards[0] - 1][dealerFaceCard - 1]
            elif softHand:
                action = Strategy.softHand2CardLookup[handTotal - 13][dealerFaceCard - 1]
            else:
                action = Strategy.hardHand2CardLookup[handTotal - 5][dealerFaceCard - 1]
        else:
            if softHand:
                action = Strategy.softHandLookup[handTotal - 13][dealerFaceCard - 1]
            else:
                action = Strategy.hardHandLookup[handTotal - 5][dealerFaceCard - 1]

        # Deviations
        if len(self.cards) == 2 and self.cards[0] == 10 and self.cards[1] == 10:
            if dealerFaceCard == 5 and trueCount >= 5:
                action = Strategy.PlayOptions.SPLIT
            elif dealerFaceCard == 6 and trueCount >= 6:
                action = Strategy.PlayOptions.SPLIT

        if handTotal == 16 and dealerFaceCard == 10 and trueCount > 0:
            action = Strategy.PlayOptions.STAY

        if handTotal == 15 and dealerFaceCard == 10 and trueCount >= 4:
            action = Strategy.PlayOptions.STAY

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
        if self.dealer.hand.cards[1] == 1 and self.shoe.getTrueCount() >= 3:
            self.insurance_bet = bet / 2.0
        else:
            self.insurance_bet = 0.0

    def playRound(self):
        bet = self.shoe.getBet()
        self.profit_from_round = 0

        if self.shoe.cardsRemaining() < 6:
            self.shoe.shuffle()
            return None

        self.player.hands = [Hand()]
        self.dealer.hand = Hand()
        self.dealFirstTwoCards()

        if not self.dealer.hand.isBlackJack():
            self.playPlayerHand(self.player.hands[0], self.dealer.hand.cards[0])
            if self.activeHands > 0:
                while True:
                    dealer_action = self.dealer.hand.dealerPlay()
                    if dealer_action == Strategy.PlayOptions.STAY:
                        break
                    elif dealer_action == Strategy.PlayOptions.HIT:
                        if self.shoe.cardsRemaining() == 0:
                            self.shoe.shuffle()
                            return None
                        self.dealer.hand.addCard(self.shoe.getCard())

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

            if move in [Strategy.PlayOptions.HIT, Strategy.PlayOptions.DOUBLE]:
                hand.addCard(self.shoe.getCard())
            elif move == Strategy.PlayOptions.SPLIT:
                break

            if move in [Strategy.PlayOptions.STAY, Strategy.PlayOptions.DOUBLE]:
                break

        if hand.getHandTotal() > 21:
            self.activeHands -= 1
            if hand.handType == HandType.DOUBLE:
                hand.result = HandResults.DOUBLELOSS
            else:
                hand.result = HandResults.LOST
        elif move == Strategy.PlayOptions.DOUBLE:
            hand.handType = HandType.DOUBLE

    def recordHandResults(self, bet):
        ph = self.player.hands[0]
        if ph.result is not None:
            if ph.result == HandResults.LOST:
                self.profit_from_round -= bet
            elif ph.result == HandResults.DOUBLELOSS:
                self.profit_from_round -= (2 * bet)
            return

        dealer_total = self.dealer.hand.getHandTotal()
        player_total = ph.getHandTotal()

        if dealer_total > 21:
            if ph.handType == HandType.DOUBLE:
                self.profit_from_round += (2 * bet)
            else:
                self.profit_from_round += bet
        else:
            if player_total == dealer_total:
                pass
            elif player_total > dealer_total:
                if ph.handType == HandType.DOUBLE:
                    self.profit_from_round += (2 * bet)
                else:
                    self.profit_from_round += bet
            else:
                if ph.handType == HandType.DOUBLE:
                    self.profit_from_round -= (2 * bet)
                else:
                    self.profit_from_round -= bet

        if ph.isBlackJack() and ph.handType == HandType.NORMAL:
            self.profit_from_round += (0.5 * bet)

###############################################
# Extended Simulation with True Count Tracking #
###############################################
def simulate_blackjack(number_of_shoes=10000):
    table = Table()
    total_profit = 0.0
    highest_true_counts = []
    lowest_true_counts = []
    total_hands = 0
    total_blackjacks = 0

    # Global extremes
    overall_max_true_count = float('-inf')
    overall_min_true_count = float('inf')
    cards_at_max_true_count = []
    cards_at_min_true_count = []

    for _shoe_idx in tqdm(range(number_of_shoes), desc="Simulating Blackjack"):
        shoe_profit = 0.0

        # Track per-shoe extremes
        max_tc = table.shoe.getTrueCount()
        min_tc = max_tc
        # We'll store the *pre-hand* composition for that round in these:
        cards_at_max_this_shoe = table.shoe.cards[:]
        cards_at_min_this_shoe = table.shoe.cards[:]

        hands_this_shoe = 0
        blackjacks_this_shoe = 0

        # Keep dealing as long as at least 6 cards remain to begin a new hand
        while table.shoe.cardsRemaining() >= 6:
            pre_hand_tc = table.shoe.getTrueCount()
            pre_hand_cards = table.shoe.cards[:]

            round_profit = table.playRound()

            # If round returns None, it means it voided mid-play (ran out of cards)
            if round_profit is None:
                break

            # If this new true count is above the shoe's current max, store it
            if pre_hand_tc > max_tc:
                max_tc = pre_hand_tc
                # Store the shoe composition from *before* the round started
                cards_at_max_this_shoe = pre_hand_cards

            # If it's below the shoe's current min, store it
            if pre_hand_tc < min_tc:
                min_tc = pre_hand_tc
                cards_at_min_this_shoe = pre_hand_cards

            shoe_profit += round_profit
            hands_this_shoe += 1

            # Count blackjacks in player's first hand
            if table.player.hands[0].isBlackJack():
                blackjacks_this_shoe += 1

        # After shoe finishes, update global extremes (and snapshots)
        if max_tc > overall_max_true_count:
            overall_max_true_count = max_tc
            cards_at_max_true_count = cards_at_max_this_shoe[:]
        if min_tc < overall_min_true_count:
            overall_min_true_count = min_tc
            cards_at_min_true_count = cards_at_min_this_shoe[:]

        highest_true_counts.append(max_tc)
        lowest_true_counts.append(min_tc)
        total_hands += hands_this_shoe
        total_blackjacks += blackjacks_this_shoe

        # Shuffle for the next shoe
        table.shoe.shuffle()
        total_profit += shoe_profit

    # Summaries
    avg_highest_true_count = sum(highest_true_counts) / len(highest_true_counts) if highest_true_counts else 0
    avg_lowest_true_count = sum(lowest_true_counts) / len(lowest_true_counts) if lowest_true_counts else 0
    avg_ev_per_shoe = total_profit / number_of_shoes if number_of_shoes else 0
    avg_hands_per_shoe = total_hands / number_of_shoes if number_of_shoes else 0
    avg_bj_per_shoe = total_blackjacks / number_of_shoes if number_of_shoes else 0

    print("Simulation Results:")
    print("-------------------")
    print(f"Highest true count seen: {overall_max_true_count}")
    print(f"Lowest true count seen: {overall_min_true_count}")
    print(f"Average highest true count per shoe: {avg_highest_true_count:.2f}")
    print(f"Average lowest true count per shoe: {avg_lowest_true_count:.2f}")
    print(f"Average EV per shoe: {avg_ev_per_shoe:.2f}")
    print(f"Average hands per shoe: {avg_hands_per_shoe:.2f}")
    print(f"Average player blackjacks per shoe: {avg_bj_per_shoe:.2f}")
    print(f"Cards left in the shoe at highest true count: {cards_at_max_true_count}")
    print(f"Cards left in the shoe at lowest true count: {cards_at_min_true_count}")

if __name__ == "__main__":
    simulate_blackjack(50000)