import pygame
from GameOfLife import Main
from miscellaneous import Buttons
pygame.init()
screenSize = 700
screen = pygame.display.set_mode((screenSize,screenSize))
pygame.display.set_caption("Game of Life 1.0")
icon = pygame.image.load("icon.PNG")
pygame.display.set_icon(icon)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (127,127,127)
YELLOW = (255,255,0)
AQUA = (0,255,255)
ORANGE = (255,165,0)
NAVY = (0,0,128)
PINK = (255,20,147)

clock = pygame.time.Clock()


def drawGrid(surface,origin,cellNumber, blockDimension, thickness = 1, colour = (255,255,255)):
    for n in range(cellNumber[0] + 1):
        pygame.draw.rect(surface, colour, (origin[0] + n * blockDimension[0], origin[1], thickness, blockDimension[1] * cellNumber[1]))
    for n in range(cellNumber[1] + 1):
        pygame.draw.rect(surface, colour, (origin[0], origin[1] + n * blockDimension[1], blockDimension[0] * cellNumber[0], thickness))

def runUpdateDraw():
    screen.fill(BLACK)
    newMatrix.display(screen,origin,cellDimension, thickness = thick)
    newMatrix.stepChange()

def setUpdate():
    global watchDog
    global watchCounter
    if pygame.mouse.get_pressed()[0]:
        mousePosition = pygame.mouse.get_pos()
        x, y = (mousePosition[0] - origin[0]) // blockDimension[0], (mousePosition[1] - origin[1]) // blockDimension[1]
        if x >= 0 and y >= 0 and (x, y) != watchDog:
            try:
                newMatrix.currentMatrix[y][x] = not newMatrix.currentMatrix[y][x]
                watchDog = (x, y)
                watchCounter = 9
            except IndexError:
                pass
        watchCounter -= 1
        if watchCounter == 0:
            watchDog = (-1, -1)
        # watchCounter and watchDog are used for debounce (prevent one click triggering the function multiple times)

def setDraw():
    global screen
    global origin
    global cellNumber
    global cellDimension
    global blockDimension
    global thick
    screen.fill(BLACK)
    newMatrix.display(screen, origin, cellDimension, thickness=thick)
    drawGrid(screen, origin, cellNumber, blockDimension, thickness=thick)

def startUpdateDraw():
    screen.fill((0, 0, 0))
    for button in startButtons:
        button.show()
    pygame.display.update()

button2 = Buttons.Button(screen, screenSize / 2, screenSize / 2 - 50, 150, 40, WHITE, GREY, BLUE, textcolour=BLACK,
                 textcolour2=BLACK, TEXT="Start")
button3 = Buttons.Button(screen, screenSize / 2, screenSize / 2, 150, 40, WHITE, GREY, BLUE, textcolour=BLACK,
                 textcolour2=BLACK, TEXT="Settings")
button4 = Buttons.Button(screen, screenSize / 2, screenSize / 2 + 50, 150, 40, WHITE, GREY, BLUE, textcolour=BLACK,
                 textcolour2=BLACK, TEXT="Quit")
startButtons = [button2, button3, button4]

newMatrix = Main.GOLMatrix(20,20)
#diehard = [(50,50),(51,50),(51,51),(56,49),(57,51),(55,51),(56,51)]
#newMatrix.initialCondition(diehard)
runButton = Buttons.Button(screen,screenSize - 50, screenSize - 50,100,40,GREY,BLUE,GREEN,TEXT = "Start")

#parameters below control which page we are currently on
runPage = False
setPage = False
startPage = True

#setPage parameters
watchDog = (-1,-1)
watchCounter = 0

#runPage parameters
Count = 0

#controls framerate per second
fps = 100

#the values below set the parameters for the size and position of grid and cells.
origin = (30,30)
cellDimension = (25,25)
cellNumber = (20,20)
thick = 2
blockDimension = (cellDimension[0] + thick, cellDimension[1] + thick)

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if runPage:
        runUpdateDraw()
        pygame.display.update()
        Count += 1

    elif setPage:
        setUpdate()
        setDraw()
        runButton.show()
        if runButton.leftClicked():
            setPage = False
            runPage = True
            fps = 3
        pygame.display.update()

    elif startPage:
        startUpdateDraw()
        if button2.leftClicked():
            setPage = True
            startPage = False
