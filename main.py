import random
import pprint

class Card:
     def values(self): return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
     def suits(self): return ['diamonds', 'hearts', 'spades', 'clubs']
     def sigils(self): return ["♦", "♥", "♠", "♣"]

     def __init__(self,value,suit):
         self.value = value
         self.suit = suit

     def __repr__(self):
         return f"({self.value}, {self.sigils()[self.suits().index(self.suit)]})"

     def isRed(self):
         if self.suits().index(self.suit) < 2: return True
         else: return False

class Board:
        foundation = [[] for i in range(4)]
        wastepile = [[]]
        face = [[] for i in range(7)]

        def __init__(self, tableau):
            self.tableau = tableau

def IsCompatible(Card1, Card2):
    if Card.isRed(Card1) ^ Card.isRed(Card2) and Card.values(Card1).index(Card1.value) == (Card.values(Card2).index(Card2.value))+1:
        return True
    else:
        return False

def CreateDeck():
    deck = [Card(value, suit) for value in Card.values(Card) for suit in Card.suits(Card)]
    random.shuffle(deck)
    return deck

def display(board):
    print(f"Foundation piles (-4; -1): {board.foundation[0]} - {board.foundation[1]} - {board.foundation[2]} - {board.foundation[3]}")
    print(f"Wastepile (0): {board.wastepile[-1]}")
    print(f"Tableau:")
    for i in range(len(board.tableau)):
        print(f"{i+1}. ({len(board.tableau[i])}) {board.face[i]}")

def turn(board):
    for i in range(len(board.face)):
        if board.face[i] == [] and len(board.tableau[i]) > 0:
            board.face[i].append(board.tableau[i].pop())
    return(board)

def draw(board, deck):
    if len(deck) > 0:
        board.wastepile.append(deck.pop())
    else:
        deck = board.wastepile[::-1]
        board.wastepile = [[]]
    return[board, deck]

def moveOne(board):
    try: colin = int(input("from: "))
    except: return board
    try: colout = int(input("to: "))
    except: return board

    if colin > 0 and colin <= len(board.tableau):
        cardout = board.face[colin].pop()
    elif colin == 0:
        if len(board.wastepile) > 0:
            cardout = board.wastepile.pop()
        else: return board

    elif colin < 0 and colin >= len(board.foundation)*-1:
        if len(board.foundation[(colin-1)*-1]) > 0:
            cardout = board.foundation[colin - 1].pop()
    else: return board

    if IsCompatible(board.face[colout-1][-1], cardout):
        board.face[colout-1].append(cardout)
        return board
    else:
        return board


# deck = CreateDeck()
# board = Board([[deck.pop() for x in range(i + 1)] for i in range(7)])
# board = turn(board)
# display(board)
# board, deck = draw(board, deck)
#
# while True:
#     board, deck = draw(board, deck)
#     board = turn(board)
#     board = moveOne(board)
#     display(board)
#     input(":")

