import random
import Player
import Board
import Box

board = None

def initGame():
    createBoard()
    assignPlayer()

def createBoard():
    global board
    cols, rows = 3, 3
    boxes = [[Box.Box() for j in range(cols)] for i in range(rows)]
    board = Board.Board(boxes, None, None)


def assignPlayer():
    global board
    namePlayer1 = input("Nom du joueur 1: ")
    namePlayer2 = input("Nom du joueur 2: ")
    if random.randint(1,2) == 1:
        player1 = Player.Player(namePlayer1, "X", True)
        player2 = Player.Player(namePlayer2, "O")
    else:
        player1 = Player.Player(namePlayer1, "O")
        player2 = Player.Player(namePlayer2, "X", True)
    board.player1 = player1
    board.player2 = player2


def queryPlay(player):
    print(player.name + " à ton tour")
    print("------------")
    endTurn = False
    while not endTurn:
        row = int(input("Quelle ligne: ")) - 1
        column = int(input("Quelle colonne: ")) - 1
        if board.playerCanPlay(row, column):
            board.playerPlay(row, column, player)
            endTurn = True
        else:
            print("Cette position n'est pas disponible")



initGame()
while board.canPlay():
    board.display()
    player = board.whosTurn()
    queryPlay(player)
    if board.playerWin(player):
        print(player.name + " vous avez remporté la partie en " + str(board.nbTurn))
        board.display()
    board.playerRotate()

