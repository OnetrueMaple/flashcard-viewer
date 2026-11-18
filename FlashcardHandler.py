import Flashcard
from random import randrange

class FlashcardHandler:
    cards = []
    currentCard = 0 # Keeps track of where you are in the list of cards.
    currentSide = 0 # 0 is front, 1 is back
    currentText = ""

    def __init__(self, arr=None):
        if(arr != None):
            for i in range(len(arr)):
                self.cards.append(arr[i])
            self.currentText = self.cards[self.currentCard].getFront()

    def getText(self):
        return self.currentText

    def swap(self):
        if(self.currentSide == 0):
            self.currentSide = 1
            self.currentText = self.cards[self.currentCard].getBack()
        else:
            self.currentSide = 0
            self.currentText = self.cards[self.currentCard].getFront()

    def next(self):
        if(self.currentCard >= len(self.cards) - 1):
            self.currentCard = self.currentCard
        else:
            self.currentCard = self.currentCard + 1
            self.currentSide = 0
            self.currentText = self.cards[self.currentCard].getFront()
            print(f"Going to next card in the list! {self.currentCard + 1}/{len(self.cards)}")

    def previous(self):
        if(self.currentCard <= 0):
            self.currentCard = self.currentCard
        else:
            self.currentCard = self.currentCard - 1
            self.currentSide = 0
            self.currentText = self.cards[self.currentCard].getFront()
            print(f"Going to previous card in the list! {self.currentCard + 1}/{len(self.cards)}")