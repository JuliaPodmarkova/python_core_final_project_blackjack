class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.is_playing = True

    def add_card(self, card):
        if card:
            self.hand.append(card)
            self.calculate_score()

    def calculate_score(self):
        self.score = 0
        ace_count = 0
        for card in self.hand:
            self.score += card.value
            if card.rank == "A":
                ace_count += 1

        while self.score > 21 and ace_count > 0:
            self.score -= 10
            ace_count -= 1

    def display_hand(self, hide_first=False):
        if hide_first:
            return "[Hidden Card], " + ", ".join(str(card) for card in self.hand[1:])
        else:
            return ", ".join(str(card) for card in self.hand)

    def has_blackjack(self):
        return len(self.hand) == 2 and self.score == 21

    def is_busted(self):
        return self.score > 21

    def reset_hand(self):
        self.hand = []
        self.score = 0
        self.is_playing = True