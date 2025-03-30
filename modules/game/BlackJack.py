import logging
import os

from modules.deck.Deck import Deck
from modules.player.Player import Player

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root1 = os.path.abspath(os.path.join(current_dir, '..'))
project_root = os.path.abspath(os.path.join(project_root1, '..'))
log_path = os.path.join(project_root, "blackjacklog.txt")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.bet = 0

    def log_message(self, message):
        print(message)
        logging.info(message)

    def start_game(self):
        self.log_message("***Start blackjack game***")
        while True:
            try:
                bet = input("PLAYER’S BET: ")
                self.log_message(f"PLAYER’S BET: {bet}")
                self.bet = int(bet)
                if self.bet > 0:
                    break
                else:
                    self.log_message("Error. WRONG INPUT:\n___player’s bet must be positive integer\nTRY AGAIN:")
            except ValueError:
                self.log_message("Error. WRONG INPUT:\n___player’s bet must be an integer\nTRY AGAIN:")


        self.player.reset_hand()
        self.dealer.reset_hand()
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

    def player_turn(self):
        self.log_message(f"___player’s bet: {self.bet} chips")
        self.log_message(f"___player’s start hand: ({self.player.display_hand()})")
        self.log_message(f"___dealer’s start hand: ({self.dealer.display_hand(hide_first=True)})")

        while self.player.is_playing:
            action = input("PLAYER’S MOVE: (hit, stand, double down): ").lower()
            self.log_message(f"PLAYER’S MOVE: {action}")

            if action == "hit":
                new_card = self.deck.deal()
                self.player.add_card(new_card)
                self.log_message(f"DEALER’S MOVE: Hit")

            elif action == "stand":
                self.player.is_playing = False
            elif action == "double down":
                self.bet *= 2
                new_card = self.deck.deal()
                self.player.add_card(new_card)
                self.player.is_playing = False
                self.log_message(f"DEALER’S MOVE: Double Down")
            else:
                self.log_message("Invalid input. Please enter 'hit', 'stand', or 'double down'.")

            if self.player.is_busted():
                self.log_message("Player Busted!")
                return False
        return True

    def dealer_turn(self):
        self.log_message(f"___player’s bet: {self.bet} chips")
        self.log_message(f"___player’s start hand: ({self.player.display_hand()})")
        self.log_message(f"___dealer’s start hand: ({self.dealer.display_hand()})")

        while self.dealer.score < 17:
            new_card = self.deck.deal()
            self.dealer.add_card(new_card)
            self.log_message(f"DEALER’S MOVE: Hit")
            self.log_message(f"___player’s bet: {self.bet} chips")
            self.log_message(f"___player’s start hand: ({self.player.display_hand()})")
            self.log_message(f"___dealer’s start hand: ({self.dealer.display_hand()})")

            if self.dealer.is_busted():
                self.log_message("Dealer Busted!")
                return

    def determine_winner(self):
        self.log_message("***Game finish***")
        self.log_message("RESULTS:")
        player_blackjack = "(blackjack)" if self.player.has_blackjack() else ""
        dealer_blackjack = "(blackjack)" if self.dealer.has_blackjack() else ""
        self.log_message(f"___player: {self.player.score} {player_blackjack}")
        self.log_message(f"___dealer: {self.dealer.score} {dealer_blackjack}")

        if self.player.is_busted():
            self.log_message("___player lost")
        elif self.dealer.is_busted():
            self.log_message("___player won")
        elif self.player.score > self.dealer.score:
            self.log_message("___player won")
        elif self.player.score < self.dealer.score:
            self.log_message("___player lost")
        else:
            self.log_message("___draw")

    def play(self):
        self.start_game()
        if self.player.has_blackjack():
            self.log_message("Blackjack!")
            self.determine_winner()
            return

        if not self.player_turn():
            self.determine_winner()
            return

        self.dealer_turn()
        self.determine_winner()

logging.shutdown()