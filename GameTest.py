import pytest

from main import *

@pytest.fixture
def board():
    return Board(CreateDeck())

def test_printcards(board):
    assert display(board)