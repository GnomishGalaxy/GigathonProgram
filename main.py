import random
import pprint


class Card:
    def values(self):
        return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def suits(self):
        return ['diamonds', 'hearts', 'spades', 'clubs']

    def sigils(self):
        return ["♦", "♥", "♠", "♣"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.numvalue = Card.values(self).index(self.value)

    def __repr__(self):
        return f"({self.value}, {self.sigils()[self.suits().index(self.suit)]})"

    def __str__(self):
        return f"({self.value}, {self.sigils()[self.suits().index(self.suit)]})"


class Board:
    foundation = [[] for i in range(4)]
    wastepile = [[]]
    face = [[] for i in range(7)]

    def __init__(self, deck):
        self.deck = deck
        self.tableau = [[deck.pop() for x in range(i + 1)] for i in range(7)]


def isRed(card):
    if card.suits().index(card.suit) < 2:
        return True
    else:
        return False


def IsCompatible(Card1, Card2):
    if isRed(Card1) ^ isRed(Card2) and Card1.numvalue == Card2.numvalue + 1:
        return True
    else:
        return False


def IsFoundationCompatible(Card1, Card2=0):
    if Card2 == 0:
        if Card1.numvalue == 0:
            return True
        else:
            return False

    if Card1.suit == Card2.suit and Card1.numvalue == Card2.numvalue + 1:
        return True
    else:
        return False


def CreateDeck():
    deck = [Card(value, suit) for value in Card.values(Card) for suit in Card.suits(Card)]
    random.shuffle(deck)
    return deck


def display(board):
    print(
        f"Foundation piles (-4; -1): {board.foundation[0]} - {board.foundation[1]} - {board.foundation[2]} - {board.foundation[3]}")
    print(f"Wastepile (0): {board.wastepile[-1]}")
    print(f"Tableau:")
    for i in range(len(board.tableau)):
        print(f"{i + 1}. ({len(board.tableau[i])}) {board.face[i]}")


def turn(board):
    for i in range(len(board.face)):
        if board.face[i] == [] and len(board.tableau[i]) > 0:
            board.face[i].append(board.tableau[i].pop())
    return (board)


def draw(board):
    if len(board.deck) > 0:
        board.wastepile.append(board.deck.pop())
    else:
        board.deck = board.wastepile[::-1]
        board.wastepile = [[]]
    return board


class EmptyWastepileException(Exception):
    pass

class ColoutZeroException(Exception):
    pass

class ColinOutOfRangeException(Exception):
    pass

class ColoutOutOfRangeException(Exception):
    pass

class MultipleCardsNotFromTableauException(Exception):
    pass

class EmptySpaceNonKingException(Exception):
    pass

class NonEmptySpaceKingException(Exception):
    pass

class TableauCardsIncompatibleException(Exception):
    pass

class FoundationIncompatibleException(Exception):
    pass


def move(board, colin, colout, amount=1):
    colin = int(colin)
    colout = int(colout)

    if colin not in range(-4, 8):
        raise ColinOutOfRangeException
    if colout not in range(-4, 8):
        raise ColoutOutOfRangeException
    if colout == 0:
        raise ColoutZeroException()
    if colin < 1 < amount:
        raise MultipleCardsNotFromTableauException

    cardin = None

    #   0 = wastepile, -4 -> -1 = foundation, 1 -> 7 = tableau
    if colin == 0:  #    from the wastepile
        if not board.wastepile:
            raise EmptyWastepileException()

        cardin = board.wastepile.pop()

    if colin < 0:  #     from the foundation
        cardin = board.foundation[abs(colin) - 1].pop()

    if colin > 0:  #     from the tableau
        cardin = board.face[colin - 1].pop()

    if colout > 0:
        if cardin.value != "K" and board.face[colout - 1] == []:
            raise EmptySpaceNonKingException

        if cardin.value == "K" and board.face[colout - 1] != []:
            raise NonEmptySpaceKingException

        if cardin.value == "K":
            board.face[colout - 1].append(cardin)
            return board

        if not IsCompatible(board.face[colout - 1][-1], cardin):
            raise TableauCardsIncompatibleException

        board.face[colout - 1].append(cardin)

    if colout < 0:
        try:
            par = board.foundation[abs(colout) - 1][-1]
        except:
            par = 0

        if IsFoundationCompatible(cardin, par):
            board.foundation[abs(colout) - 1].append(cardin)
        else:
            raise FoundationIncompatibleException

    return board