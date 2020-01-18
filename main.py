from Crossword import Collect
import string
import time
import random

class directions:
    RIGHT = 0
    DOWN = 1

class Crossword:
    def __init__(self, words, board):
        self.words = words
        self.board = board
        self.height = len(self.board)
        self.width = len(self.board[0])

        self.word = []
        self.tiles = []
        for x in range(self.width):
            self.tiles.append([])
            for y in range(self.height):
                self.tiles[x].append(None)

    def __str__(self):
        tiles = list(zip(*self.tiles))
        return '\n'.join([
            ''.join([
                tile == None and "#" or (
                    len(tile.chars) == 0 and "-" or 
                    len(tile.chars) == 1 and tile.chars[0] or
                    '['+''.join(tile.chars)+']'
                ) for tile in row
            ])
            for row in tiles
        ])

    def generateWords(self, limit=1):
        # get horizontal words
        for x in range(self.width):
            wordStart = True
            for y in range(self.height):
                if self.isWall(x, y):
                    wordStart = True
                elif wordStart:
                    wordStart = False

                    word = Word(
                        board=self,
                        x=x,
                        y=y,
                        direction=directions.DOWN
                    )

                    if word.length > limit:
                        word.claim()
                        self.word.append(word)

        # get vertical words
        for y in range(self.height):
            wordStart = True
            for x in range(self.width):
                if self.isWall(x, y):
                    wordStart = True
                elif wordStart:
                    wordStart = False

                    word = Word(
                        board=self,
                        x = x,
                        y = y,
                        direction=directions.RIGHT
                    )

                    if word.length > limit:
                        word.claim()
                        self.word.append(word)

    def populateWords(self):
        word = self.word[0]
        word.populate()

    def chooseWords(self):
        i = 0
        while i < len(self.word):
            if len(self.word[i].words) > 1:
                self.word[i].select()
            i += 1

    def getTile(self, x, y):
        if self.tiles[x][y] == None:
            self.tiles[x][y] = Tile(
                board=self,
                x=x,
                y=y
            )
        return self.tiles[x][y]

    def isWall(self, x, y):
        return self.board[y][x] == "#"

    def cheakWord(self, word, tiles):
        if len(word) != len(tiles):
                return False
            
        for i in range(len(word)):
            if word[i] not in tiles[i].chars:
                return False

        return True

    def getWords(self, tiles):
        words = []
        for word in self.words:
            if self.cheakWord(word, tiles):
                words.append(word)
        return words

class Word:
    def __init__(self, board, x, y, direction):
        self.board = board
        self.x = x
        self.y = y
        self.direction = direction
        self.selected = False
        self.words = []

        self.length = 0
        self.tiles = []

        if self.direction == directions.RIGHT:
            pos = self.x
            while pos < board.width and not self.board.isWall(pos, self.y):
                pos += 1
                self.length += 1


        if self.direction == directions.DOWN:
            pos = self.y 
            while pos < board.height and not self.board.isWall(self.x, pos):
                pos += 1
                self.length += 1

    def claim(self):
        for i in range(self.length):
            if self.direction == directions.RIGHT:
                self.addTile(self.board.getTile(self.x + i, self.y), i)

            if self.direction == directions.DOWN:
                self.addTile(self.board.getTile(self.x, self.y + i), i)

    def addTile(self, tile, pos):
        tile.words[self] = pos
        self.tiles.append(tile)

    def populate(self):
        if not self.selected:
            old = self.words
            self.words = self.board.getWords(self.tiles)
            print(list(set(old) - set(self.words)))
        for tile in self.tiles:
            tile.limit(self)

    def select(self):
        if len(self.words) <= 1:
            print("attemted to select word with one word!")
            return
        self.selected = True
        #self.words = [self.words[random.randint(0,len(self.words) - 1)]]
        self.words = [self.words[0]]
        self.populate()

class Tile:
    def __init__(self, board, x, y, chars=list(string.ascii_lowercase)):
        self.board = board
        self.x = x
        self.y = y
        self.chars = chars
        self.words = {}

    def shouldReaload(self, chars):
        for char in self.chars: 
            if char not in chars:
                return True
        
        return False

    def limit(self, word):
        chars = []
        for w in word.words:
            char = w[self.words[word]]
            if char not in chars:
                chars.append(char)

        if self.shouldReaload(chars):
            self.chars = chars

            print(self.board)
            print()

            for w in self.words:
                if w is not word:
                    w.populate()

def test(words, board, expected):
    print("----------------------")
    crossword = Crossword(
        words=words,
        board=board
    )
    crossword.generateWords()
    crossword.populateWords()

    print(crossword)
    print()

    if True:
        crossword.chooseWords()

        print(crossword)
        print()


if __name__ == "__main__":
    test(
        words = [
            "card",
            "over",
            "lily",
            "dde",

            "cold",
            "avid",
            "rele",
            "dry"
        ],
        board = [
            "    ",
            "    ",
            "    ",
            "   #"
        ],
        expected = [
            "card",
            "over",
            "lily",
            "dde#"
            
        ]
    )

    
    