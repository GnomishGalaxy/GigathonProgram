from main import Card
import pytest

def test_isred_1():
    card1 = Card(2, "hearts")
    card2 = Card(2, "spades")
    assert Card.isRed(card1) == True
    assert Card.isRed(card2) == False

def test_printcards():
    card1 = Card(2, "hearts")
    card2 = Card(2, "spades")