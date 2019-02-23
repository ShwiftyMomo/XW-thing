from Crossword import Collect

class Crossword:
    def __init__(this, words, board):
        this.words = words
        this.board = board

    def __str__(this):
        return ''.join([''.join(row) + "\n" for row in this.board])

class Word:
    def __init__(this):
        pass

class Tile:
    def __init__(this):
        pass

if __name__ == "__main__":
    words = Collect()
    board = [
        [' ','#',' ',' ',' ','#',' ',' ',' '],
        [' ','#',' ',' ',' ','#',' ',' ',' '],
        [' ','#',' ',' ',' ','#',' ',' ',' '],
        [' ',' ',' ',' ',' ','#','#',' ','#'],
        ['#','#',' ','#','#','#','#',' ','#'],
        ['#','#',' ','#',' ',' ',' ',' ',' '],
        [' ',' ',' ','#',' ',' ',' ',' ',' '],
        ['#','#',' ',' ',' ',' ',' ',' ',' '],
    ]
    print(Crossword(
        words=words,
        board=board
    ))