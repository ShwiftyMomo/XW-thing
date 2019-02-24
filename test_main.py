import unittest
import main

class TestCrossword(unittest.TestCase):
    def test_init(self):
        board = main.Crossword(
            words = [
                "a"
            ],
            board = [
                [" "," "," "," "," "]
            ]
        )

        self.assertEqual(board.width, 5)
        self.assertEqual(board.height, 1)
        self.assertEqual(board.words, ["a"])

    def test_generateWords(self):
        board = main.Crossword(
            words = [],
            board = [
                [" "," "," "," "," "]
            ]
        )
        board.generateWords()
        self.assertEqual(len(board.word), 1)

        board = main.Crossword(
            words = [],
            board = [
                [" "," "," "],
                [" "," "," "],
                [" "," "," "]
            ]
        )
        board.generateWords()
        self.assertEqual(len(board.word), 6)

        board = main.Crossword(
            words = [],
            board = [
                [" "," "," "],
                [" ","#","#"],
                [" ","#","#"]
            ]
        )
        board.generateWords()
        self.assertEqual(len(board.word), 2)

    def test_populateWords(self):
        pass

    def test_getTile(self):
        pass

    def test_isWall(self):
        board = main.Crossword(
            words = [],
            board = [
                [" ","#"," "],
                ["#"," ","#"]
            ]
        )

        self.assertFalse(board.isWall(0,0))
        self.assertTrue(board.isWall(1,0))
        self.assertTrue(board.isWall(0,1))
        self.assertFalse(board.isWall(1,1))
        self.assertTrue(board.isWall(2,1))

    def test_getWords(self):
        board = main.Crossword(
            words = [
                "aaaaa",
                "aaa",
                "abcd",
                "aaaa"
            ],
            board = [
                [" "],
            ]
        )

        self.assertEqual(board.getWords(
            [
                main.Tile(board, 0, 0),
                main.Tile(board, 0, 1),
                main.Tile(board, 0, 1)
            ]
        ), ["aaa"])

        self.assertEqual(board.getWords(
            [
                main.Tile(board, 0, 0),
                main.Tile(board, 0, 1),
                main.Tile(board, 0, 2),
                main.Tile(board, 0, 3)
            ]
        ), ["abcd", "aaaa"])

        self.assertEqual(board.getWords(
            [
                main.Tile(board, 0, 0),
                main.Tile(board, 0, 1),
                main.Tile(board, 0, 2),
                main.Tile(board, 0, 3, ["a"])
            ]
        ), ["aaaa"])

class TestWord(unittest.TestCase):
    def test_populate(self):
        pass

class TestTile(unittest.TestCase):
    def test_limit(self):
        '''board = main.Crossword(
            board=[
                []
            ],
            words=[]
        )
        word = main.Word(
            board=board,
            x=0,
            y=0,
            direction=main.directions.DOWN
        )'''
        pass

if __name__ == "__main__":
    unittest.main()