import Player

class Board:
    def __init__(self, boxes, player1, player2):
        self.boxes = boxes
        self.player1 = player1
        self.player2 = player2
        self.nbTurn = 0
        self.hasWin = False

    def canPlay(self):
        canPlay = False
        if not self.hasWin:
            for row in self.boxes:
                for column in self.boxes[self.boxes.index(row)]:
                    if column.type == "empty":
                        canPlay = True
                        break
        return canPlay

    def playerCanPlay(self, row, column):
        canPlay = False
        if self.boxes[row][column].type == "empty":
            canPlay = True
        return canPlay

    def playerPlay(self, row, column, player):
        self.boxes[row][column].type = player.type
        self.nbTurn += 1

    def display(self):
        for row in self.boxes:
            displayed_row = ""
            for column in self.boxes[self.boxes.index(row)]:
                if column.type == "empty":
                    displayed_row += " _ "
                else:
                    displayed_row += " " + column.type + " "
            print(displayed_row)
    
    def playerRotate(self):
        if self.player1.hisTurn:
            self.player1.hisTurn = False
            self.player2.hisTurn = True
        else:
            self.player1.hisTurn = True
            self.player2.hisTurn = False

    def whosTurn(self):
        if self.player1.hisTurn:
            return self.player1
        else:
            return self.player2

    def playerWin(self, player):
        hasWin = False
        if self.winHorizontal(player.type) | self.winVertical(player.type) | self.winDiagonal(player.type):
            hasWin = True
            self.hasWin = True
        return hasWin

    def winHorizontal(self, type):
        nbType = 0
        hasWin = False
        for row in self.boxes:
            nbType = 0
            if not hasWin:
                for column in self.boxes[self.boxes.index(row)]:
                    if column.type == type:
                        nbType += 1
                if nbType == 3:
                    hasWin = True
            else:
                break
        return hasWin

    def winVertical(self, type):
        nbType = 0
        hasWin = False
        for nbColumn in range(len(self.boxes[0])):
            nbType = 0
            if not hasWin:
                for row in self.boxes:
                    if row[nbColumn].type == type:
                        nbType += 1
                if nbType == 3:
                    hasWin = True
            else:
                break
        return hasWin

    def winDiagonal(self, type):
        hasWin = False
        index = 0
        nbType = 0
        for row in self.boxes:
            if not hasWin:
                if row[index].type == type:
                    nbType += 1
                index += 1
                if nbType == 3:
                    hasWin = True
            else:
                break
        if not hasWin:
            index = 2
            nbType = 0
            for row in self.boxes:
                if not hasWin:
                    if row[index].type == type:
                        nbType += 1
                    index -= 1
                    if nbType == 3:
                        hasWin = True
                else:
                    break
        return hasWin
