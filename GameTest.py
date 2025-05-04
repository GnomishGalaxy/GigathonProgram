import pytest

from main import *

@pytest.fixture
def board():
    return Board(CreateDeck())
random.seed(42)

def test_printcards(board):
    assert str(board.deck[0]) == "(3, ♥)"

def test_turn(board):
    board = turn(board)
    assert board.face[0] == Card
    assert board.face[1] == Card
    assert board.face[2] == Card