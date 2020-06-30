from random import shuffle

class Desk:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def re_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()