from unittest import TestCase
from main import Card

class TestCard(TestCase):
    def test_create(self):
        self.value = 'A'
        self.suit = 'hearts'


    def test_checkRed(self):
        self.value = '2'
        self.suit = 'hearts'
        print(f"{self.suit}, {Card.isRed(self)}")

        self.suit = 'clubs'
        print(f"{self.suit}, {Card.isRed(self)}")

        self.suit = 'diamonds'
        print(f"{self.suit}, {Card.isRed(self)}")

        self.suit = 'spades'
        print(f"{self.suit}, {Card.isRed(self)}")