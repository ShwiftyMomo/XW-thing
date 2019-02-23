#Imports
import random as r
import numpy as np
#Makeing the alphabet
alph = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
#Checking if an individual word fits a criteria
def Check(word,criterias):
    if len(word) != len(criteria):
        return False
    for letter in criteria:
        if type(letter) == str:
            letter = [letter]
        if letter != "." and letter not in word[k]:
                return False
        return True
#Cleans data: Removes 3 letter words+ Proper Nouns
def Cleanse(SomeData):
    Newdata = []
    for word in SomeData:
        word = word[:-1]
        if not len(word)<3 and not word[0].isupper():
            Newdata.append(word)
    return Newdata
#Defining A Database-Wide Search for fits
def Search(SomeData,criteria):
    Fits = []
    for word in SomeData:
        if Check(word,criteria):
            Fits.append(word)
    return Fits
#FullData
def Collect():
    RawDatabase = open("/usr/share/dict/words", "r")
    return Cleanse(RawDatabase.readlines())
#Defining the Crossword-Board class
#class Board:
    #Define the Crossword's variables
    def __init__(self,size):
        # All the squares on the board
        self.sq = np.empty((size,size), dtype = object)
        #The size of the board
        self.size = size
        #The array with the list of possible letters for every square
        self.lett = np.empty((size,size,26), dtype = object)
        #The Words, in format [[startX,startY],length,direction]
        self.wrds = []
    #Make the Crossword printable
    def __str__(self):
        return str(self.sq)
    #The flipped-about-the-center of an element x
    def inv(self,x):
        return self.size - x-1
    #Places the black squares
    def Populate(self):
        for i in range(self.size**2//8+ r.randint(0,self.size**2/9)):
            x = r.randint(0,self.size-1)
            y = r.randint(0,self.size-1)
            self.sq[x][y] = '-'
            self.sq[self.inv(x)][self.inv(y)] = '-'
    #Sets up the 'lett'
    def LettSet(self):
        for row in self.lett:
            for sets in row:
                sets =  "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    #Finds the length of a word
    def findword(self,x,y,booly):
        i = 0
        if not booly:
            while self.sq[x][y + i] == None:
                i+=1
                if y+i == self.size:
                    break
        else:
            while self.sq[x+i][y] == None:
                i+=1
                if x+i == self.size:
                    break

        return [[x,y],i,booly]
    #Sets up the 'wrds'
    def WrdsSet(self):
        #Gets all words that dont start at the edges
        for i in range(self.size-1):
            for j in range(self.size-1):
                if self.sq[i][j] == None:
                    if self.sq[i][j-1] == '-' and self.sq[i][j+1] == None:
                        self.wrds.append(self.findword(i,j,1))
                    if self.sq[i-1][j] == '-' and self.sq[i+1][j] == None:
                        self.wrds.append(self.findword(i,j,0))
        #Gets the words that start at edges
        for i in range(self.size):
            if self.sq[0][i] == None and self.sq[1][i]==None:
                self.wrds.append(self.findword(0,i,0))
            if self.sq[i][0] == None and self.sq[i][1] == None:
                self.wrds.append(self.findword(i,0,1))
    #Calls all the setup functions
    def FullSetup(self):
        self.Populate()
        self.LettSet()
        self.WrdsSet()
#Temporary Stuff
"""B=Board(15)
B.FullSetup()
print(B)
print(B.wrds)
print(len(B.wrds))"""
print(1 in [1,2])
