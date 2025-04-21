import pytest

from main import Card
from main import Board


@pytest.fixture
def board():
    return Board()

def test_printcards(board):
    assert board.printcards() == []