import pygame
pygame.init()

run = True
screen_W = 800
screen_H = 600
screen_Color = "Black"
#screen = pygame.display.set_mode((screen_W, screen_H))

boardColor1 = "tan"
boardColor2 = "brown"
boardWidth = 8
boardHeight = 8
boardX = 0
boardY = 0

squareWidth = 64
squareHeight = 64


class Screen:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))
        self.color = self.display.fill(color)
    #def display(self, width, height):
        #pygame.display.set_mode((width, height))

#board class
class Board:
    def __inti__(self, rows, surface, firstRowColor, width, height, X_pos, Y_pos, squares_in_row, rows_in_board):
        self.rows = rows
        self.surface = surface
        self.firstRowColor = firstRowColor
        self.width = width
        self.height = height
        self.X_pos = X_pos
        self.Y_pos = Y_pos
        self.squares_in_row = squares_in_row
        self.rows_in_board = rows_in_board
    def drawBoard(self):
        lastY = self.Y_pos
        currentRowColor = alternateColor(self.firstRowColor)
        while rows_in_board > 0:
            currentRowColor = alternateColor(currentRowColor)
            drawRow(self.surface, currentRowColor, self.width, self.height, self.X_pos, lastY, self.squares_in_row)
            lastY = lastY + self.height
            rows_in_board = rows_in_board -1

#row class
            
class Row:
    def __init__(self, squares, surface, firstSquareColor, width, height, X_pos, Y_pos):
        self.squares = squares
        self.surface = surface
        self.firstSquareColor = firstSquareColor
        self.width = width
        self.height = height
        self.X_pos = X_pos
        self.Y_pos = Y_pos

    def drawRow(self):
        lastX = self.X_pos
        currentColor = alternateColor(self.firstSquareColor)
        for Square in self.squares:
            currentColor = alternateColor(currentColor)
            x = Square(self.surface, currentColor, self.width, self.height, lastX, self.Y_pos)
            x.draw()
            lastX = lastX + self.width


class Square:
    def __init__(self, surface, color, width, height, X_pos, Y_pos):
        self.surface = surface
        self.color = color
        self.width = width
        self.height = height
        self.X_pos = X_pos
        self.Y_pos = Y_pos
    def draw(self):
        square = pygame.Rect((self.X_pos, self.Y_pos, self.width, self.height))
        pygame.draw.rect(self.surface, (self.color), square)


def alternateColor(color):
    if color == boardColor1:
        color = boardColor2
    else:
        color = boardColor1
    return(color)


def centerBoard(boardHeight, boardWidth, squareHeight, squareWidth, screen_H, screen_W):
    #center X
    pixelsX = boardWidth*squareWidth
    remainingpixelsX = screen_W - pixelsX
    xOffset = remainingpixelsX/2
    
    #center Y
    pixelsY = boardHeight*squareHeight
    remainingpixelsY = screen_H - pixelsY
    yOffset = remainingpixelsY/2

    return(xOffset, yOffset)

def drawRow(surface, firstSquareColor, width, height, X_pos, Y_pos, squares_in_row):
    lastX = X_pos
    currentColor = alternateColor(firstSquareColor)
    while squares_in_row>0:
        currentColor = alternateColor(currentColor)
        x = Square(surface, currentColor, width, height, lastX, Y_pos)
        x.draw()
        lastX = lastX + width
        squares_in_row = squares_in_row - 1

def drawBoard(surface, firstRowColor, width, height, X_pos, Y_pos, squares_in_row, rows_in_board):
    lastY = Y_pos
    currentRowColor = alternateColor(firstRowColor)
    while rows_in_board > 0:
        currentRowColor = alternateColor(currentRowColor)
        drawRow(surface, currentRowColor, width, height, X_pos, lastY, squares_in_row)
        lastY = lastY + height
        rows_in_board = rows_in_board -1


placement = list(centerBoard(boardHeight, boardWidth, squareHeight, squareWidth, screen_H, screen_W))
boardX = placement[0]
boardY = placement[1]


Chess_Screen = Screen(screen_W, screen_H, "Black")
#Chess_Screen.display.fill("grey")
drawBoard(Chess_Screen.display, boardColor1, squareWidth, squareHeight, boardX, boardY, boardWidth, boardHeight)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()



#draw row
    #this function takes in the total width of the board, and draws that many squares next to each other
    #it also takes in an X and Y starting location
    #inputs: Xpos, Ypos, Square_Wdith, Square_Height, quantity, color1, color2

    #but if we think about this function less as drawing squares, and more about altering objects that already exist, that changes things


    #1: we want to create a class called square
    #2: we want to draw a board
        #2a: we want to initialize a bunch of sqaures in a row, each with starting distances offset from the last square
        #2b: reapeat 2a until we have as many rows as there are in the height
    

    #create square: the class that 
    #create row:
