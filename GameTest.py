import pytest

from main import *

@pytest.fixture
def board():
    random.seed(6)
    return Board(CreateDeck())


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
    assert (board.wastepile[-1].suit == "spades"
        and board.wastepile[-1].value == "9")

def test_compatibility():
    card1 = Card("2", "hearts")
    card2 = Card("3", "spades")
    card3 = Card("3", "diamonds")

    assert IsCompatible(card2, card1) # right values, right colors
    assert not IsCompatible(card1, card2) # right colors, wrong values
    assert not IsCompatible(card3, card1) # wrong colors, right values

def test_pop2(board):
    assert len(board.deck) == 24


@pytest.fixture
def board():
    random.seed(6)
    return Board(CreateDeck())

def test_move_fail(board):
    board = turn(board)
    assert not move(board, "lorem", "ipsum")
    assert not move(board, 1, 50)
    assert not move(board, -50, 1)
    assert not move(board, 2, 0)
    assert not move(board, 0, 1)
    board.face[0] = []
    assert not move(board, 1, 2)

def test_move(board):
    board = turn(board)
    board = move(board, 2, 7)
    assert (board.face[6][-1].suit == "hearts"
            and board.face[6][-1].value == "2")

def test_move_king(board):
    board = turn(board)
    board.face[1] = []

    board = move(board, 1, 2)
    assert (board.face[1][-1].suit == "spades"
            and board.face[1][-1].value == "K")

def test_move_wastepile(board):
    board = turn(board)
    board = draw(board)
    board = move(board, 0, 4)
    assert board.face[3][-1].suit == "spades"
    assert board.face[3][-1].value == "9"

def test_move_foundation(board):
    board = turn(board)
    board = move(board, 1, -4)
    display(board)
    assert board.foundation[3][-1].suit == "spades"
    assert board.foundation[3][-1].value == "9"