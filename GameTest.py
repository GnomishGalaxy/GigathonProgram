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
    with pytest.raises(ValueError):
        move(board, "lorem", "ipsum")
    with pytest.raises(ColoutOutOfRangeException):
        move(board, 1, 50)
    with pytest.raises(ColinOutOfRangeException):
        move(board, -50, 1)
    with pytest.raises(ColoutZeroException):
        move(board, 2, 0)
    with pytest.raises(TableauCardsIncompatibleException):
        move(board, 0, 1)

    board.face[0] = []
    with pytest.raises(IndexError):
        move(board, 1, 2)
    with pytest.raises(EmptySpaceNonKingException):
        move(board, 2, 1)

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
    assert (board.face[3][-1].suit == "spades"
            and board.face[3][-1].value == "9")

def test_move_foundation(board):
    for i in range(6):
        board = draw(board)
    board = turn(board)

    board = move(board, 0, -4)
    assert (board.foundation[3][-1].suit == "clubs"
            and board.foundation[3][-1].value == "A")

    board = move(board, 3, -3)
    assert (board.foundation[2][-1].suit == "spades"
            and board.foundation[2][-1].value == "A")

    board.foundation[1] = [Card("A", "hearts")]
    board = move(board, 7, -2)
    assert (board.foundation[1][-1].suit == "hearts"
            and board.foundation[1][-1].value == "2")