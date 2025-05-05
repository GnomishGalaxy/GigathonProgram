import pytest

from main import *

@pytest.fixture
def board():
    return Board(CreateDeck())
random.seed(6)

def test_printcards(board):
    assert (board.deck[-1].suit == "spades"
        and board.deck[-1].value == "9")

def test_pop(board):
    assert len(board.deck) == 24

def test_turn(board):
    board = turn(board)
    assert type(board.face[0][0]) == Card
    assert type(board.face[6][0]) == Card

def test_draw_wastepile(board):
    board = draw(board)
    assert (board.wastepile[-1].suit == "clubs"
        and board.wastepile[-1].value == "4")
    display(board)

def test_compatibility():
    card1 = Card("2", "hearts")
    card2 = Card("3", "spades")
    card3 = Card("3", "diamonds")

    assert IsCompatible(card2, card1) # right values, right colors
    assert not IsCompatible(card1, card2) # right colors, wrong values
    assert not IsCompatible(card3, card1) # wrong colors, right values

def test_pop2(board):
    assert len(board.deck) == 24

def test_move(board):
    assert not moveOne(board, "lorem", "ipsum")
    assert not moveOne(board, 1, 50)
    assert not moveOne(board, -50, 1)
    assert not moveOne(board, 2, 0)
    assert not moveOne(board, 0, 1)

    board = moveOne(board, 4, 3)
    assert (board.tableau[2][-1].suit == "diamonds"
            and board.tableau[2][-1].suit == "3")

    board.tableau[7] = []
    board = moveOne(board, 1, 7)
    assert (board.tableau[6][-1].suit == "spades"
            and board.tableau[6][-1].suit == "K")

