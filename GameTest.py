import pytest

from main import *

@pytest.fixture
def board():
    return Board(CreateDeck())
random.seed(42)

def test_printcards(board):
    assert str(board.deck[0]) == "(3, ♥)"

def test_pop(board):
    assert len(board.deck) == 24

def test_turn(board):
    board = turn(board)
    assert type(board.face[0][0]) == Card
    assert type(board.face[6][0]) == Card

def test_draw_wastepile(board):
    board = draw(board)