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

def IsFoundationCompatible(Card1, Card2 = 0):
    if Card2 == 0:
        if Card1.numvalue == 1:
            return True
        else:
            return False

    if Card1.suit == Card2.suit and Card1.numvalue + 1 == Card2.numvalue:
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


def move(board, colin, colout, amount = 1):
    try:
        colin = int(colin)
    except:
        return False
    try:
        colout = int(colout)
    except:
        return False

    if colin < -4 or colin > 7 or colout > 7 or colout < -4 or colout == 0: return "boog"
    if colin < 1 and amount > 1: return "boog"

    #   0 = wastepile, -4 -> -1 = foundation, 1 -> 7 = tableau
    if colin == 0:  #    from the wastepile
        if board.wastepile != []:
            cardin = board.wastepile.pop()
        else:
            return "Sloog"
    if colin < 0:  #     from the foundation
        try:
            cardin = board.foundation[abs(colin)-1].pop()
        except: return "Slag"
    if colin > 0:  #     from the tableau
        try:
            cardin = board.face[colin - 1].pop()
        except: return "slonk"

    if colout > 0:
        if cardin.value == "K":
            if board.face[colout - 1] == []:
                board.face[colout - 1].append(cardin)
                return board
            else:
                return False
        elif board.face[colout - 1] == []:
            return False

        if IsCompatible(board.face[colout-1][-1], cardin):
            board.face[colout-1].append(cardin)
        else:
            return False
    if colout < 0:
        if IsFoundationCompatible(cardin, board.foundation[abs(colout)-1][-1]):
            board.foundation[abs(colout)-1].append(cardin)
        else:
            return False

    return board

# board = Board(CreateDeck())
# board = turn(board)
# display(board)
# board= draw(board)

# while True:
#     board, deck = draw(board, deck)
#     board = turn(board)
#     board = move(board)
#     display(board)
#     input(":")
