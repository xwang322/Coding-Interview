'''
设计一个战棋游戏，主要是保存状态还有决定谁赢了, 类似battleship
'''
import sys
import collections
import random
class Player(object):
    def __init__(self, id):
        self.id = id
        self.side = 5

    def PlaceShip(self, length):
        horizontal = random.randint(0, self.side-1)
        vertical = random.randint(0, self.side-1)
        direction = random.randint(0, 1)
        if direction:
            print ('Your ship is placed at '+str(horizontal) + ', ' + str(vertical) + ', ' + 'horizontally')
            return (horizontal, vertical, True)
        else:
            print ('Your ship is placed at '+str(horizontal) + ', ' + str(vertical) + ', ' + 'vertically')
            return (horizontal, vertical, False)

class Battleship(object):
    def __init__(self):
        self.side = 5
        self.board = [[0 for i in range(self.side)] for j in range(self.side)]
        self.ships = [0, 1, 2]
        self.players = [Player(i) for i in range(2)]
        self.boatsposition1 = collections.defaultdict(list)
        self.boatsposition2 = collections.defaultdict(list)
        self.bombpositions = set()

    def PlaceBattleShip(self):
        for i in range(len(self.players)):
            for j in range(len(self.ships)):
                length = self.ships[j]+1
                flag = False
                while not flag:
                    setup = self.players[i].PlaceShip(length)
                    if self.CheckBoardPosition(setup, length):
                        self.SetBoardPosition(i, setup, length)
                        flag = True

    def CheckBoardPosition(self, setup, length):
        s1, s2, s3 = setup[0], setup[1], setup[2]
        if s3:
            if s2+length <= self.side:
                temp_matrix = []
                for j in range(s2, s2+length):
                    temp_matrix.append(self.board[s1][j])
                return all(element == 0 for element in temp_matrix)
        else:
            if s1+length <= self.side:
                temp_matrix = []
                for j in range(s1, s1+length):
                    temp_matrix.append(self.board[j][s2])
                return all(element == 0 for element in temp_matrix)
        return False

    def SetBoardPosition(self, i, setup, length):
        s1, s2, s3 = setup[0], setup[1], setup[2]
        if s3:
            for j in range(s2, s2+length):
                self.board[s1][j] = i+1
                if i == 0:
                    self.boatsposition1[length-1].append((s1, j))
                else:
                    self.boatsposition2[length-1].append((s1, j))
        else:
            for j in range(s1, s1+length):
                self.board[j][s2] = i+1
                if i == 0:
                    self.boatsposition1[length-1].append((j, s2))
                else:
                    self.boatsposition2[length-1].append((s1, j))

    def PlayGame(self):
        while not self.CheckIfWin():
            for i in range(len(self.players)):
                position = None
                while not position:
                    position = self.ChooseBombPosition()
                self.DropBomb(i, position)
                if self.CheckAWinner(i):
                    print 'Player %d has won' %(i+1)
                    print self.board
                    return

    def CheckIfWin(self):
        player = [1,2]
        for i in player:
            temp = 3- i
            if any(temp in sublist for sublist in self.board):
                return False
        return True

    def CheckAWinner(self, player):
        player += 1
        temp = 3 - player
        if not any(temp in sublist for sublist in self.board):
            return True
        return False

    def ChooseBombPosition(self):
        horizontal = random.randint(0, self.side-1)
        vertical = random.randint(0, self.side-1)
        if (horizontal, vertical) not in self.bombpositions:
            #print ('Your bomb is placed at ' +  str(horizontal) + ',' + str(vertical))
            self.bombpositions.add((horizontal, vertical))
            return (horizontal, vertical)
        else:
            return None

    def DropBomb(self, player, position):
        if self.board[position[0]][position[1]] != 0:
            boatindex = None
            if self.board[position[0]][position[1]] == 1:
                for i in self.boatsposition1:
                    if (position[0], position[1]) in self.boatsposition1[i]:
                        boatindex = i
                if boatindex:
                    self.boatsposition1[boatindex].remove((position[0], position[1]))
                    if self.boatsposition1[boatindex] == None:
                        del self.boatsposition1[boatindex]
            else:
                for i in self.boatsposition2:
                    if (position[0], position[1]) in self.boatsposition2[i]:
                        boatindex = i
                if boatindex:
                    self.boatsposition2[boatindex].remove((position[0], position[1]))
                    if self.boatsposition2[boatindex] == None:
                        del self.boatsposition2[boatindex]
            self.board[position[0]][position[1]] = 0


game = Battleship()
game.PlaceBattleShip()
print (game.board)
game.PlayGame()
