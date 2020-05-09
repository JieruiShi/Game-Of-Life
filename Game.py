import pygame
import Main
import Buttons


#region initialize screen,window,colour
pygame.init()
screenSize = 750
screen = pygame.display.set_mode((screenSize,screenSize))
pygame.display.set_caption("Game of Life 1.1")
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
#endregion

clock = pygame.time.Clock()


def drawGrid(surface,origin,cellNumber, blockDimension, thickness = 1, colour = (255,255,255)):
    for n in range(cellNumber[0] + 1):
        pygame.draw.rect(surface, colour, (origin[0] + n * blockDimension[0], origin[1], thickness, blockDimension[1] * cellNumber[1]))
    for n in range(cellNumber[1] + 1):
        pygame.draw.rect(surface, colour, (origin[0], origin[1] + n * blockDimension[1], blockDimension[0] * cellNumber[0], thickness))

def showWord(text,position,colour = WHITE, size = 20):
    myFont = pygame.font.SysFont("Times New Roman", size)
    myText = myFont.render(text,True,colour)
    screen.blit(myText,position)

#region runPage
def runUpdateDraw():
    screen.fill(BLACK)
    newMatrix.display(screen,origin,cellDimension, thickness = thick)
    newMatrix.stepChange()

#runPage parameters
Count = 0
#endregion

#region setPage
def setUpdate():
    global watchDog
    global watchCounter
    if pygame.mouse.get_pressed()[0]:
        mousePosition = pygame.mouse.get_pos()
        #to prevent clicking on menu triggers the cell update
        if pygame.mouse.get_pos()[0]< (origin[0] + blockDimension[0] * cellNumber[0]) and pygame.mouse.get_pos()[1]< (origin[1] + blockDimension[1] * cellNumber[1]):
            x, y = (mousePosition[0] - origin[0]) // blockDimension[0], (mousePosition[1] - origin[1]) // blockDimension[1]
            if x >= 0 and y >= 0 and (x, y) != watchDog:
                try:
                    newMatrix.currentMatrix[y][x] = not newMatrix.currentMatrix[y][x]
                    watchDog = (x, y)
                    watchCounter = 12
                except IndexError:
                    pass
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
    showWord("Grid Size: {}".format(gridSize),(screenSize - 120,screenSize - 210),colour = AQUA, size = 22)
    for button in runButtons:
        button.show()

def setSizeChange(gridSize):
    global cellDimension
    global cellNumber
    global thick
    global blockDimension
    gridDimension = list_of_size[gridSize]
    cellDimension = (gridDimension[0], gridDimension[0])
    cellNumber = (gridDimension[1], gridDimension[1])
    thick = gridDimension[2]
    blockDimension = (cellDimension[0] + thick, cellDimension[1] + thick)
    newMatrix.reshape(gridDimension[1], gridDimension[1])

#region setPage button & parameters
button1 = Buttons.Button(screen,screenSize - 70, screenSize - 50,100,40,GREY,BLUE,GREEN,TEXT = "Start")
button5 = Buttons.Button(screen,screenSize - 100, screenSize - 150,40,40,GREY,BLUE,GREEN,TEXT = "◄")
button6 = Buttons.Button(screen,screenSize - 40, screenSize - 150,40,40,GREY,BLUE,GREEN,TEXT = "►")
button7 = Buttons.Button(screen,screenSize - 70, screenSize - 100,100,40,GREY,BLUE,GREEN,TEXT = "Centralize")
runButtons = [button1,button5,button6,button7]
watchDog = (-1,-1)
watchCounter = 0
#endregion

#along with button5,button6, parameters that control gridsize.
list_of_size = [(4,120,1),(7,75,1),(9,60,1),(11,50,1),(13,40,2),(18,30,2),(23,24,2),(27,20,3),(36,15,4),(55,10,5)]
origin = (10,10)
cellDimension = (23,23)
cellNumber = (24,24)
thick = 2
blockDimension = (cellDimension[0] + thick, cellDimension[1] + thick)
gridSize = 7

#endregion

#region startPage
def startUpdateDraw():
    screen.fill((0, 0, 0))
    for button in startButtons:
        button.show()
    pygame.display.update()

#region startPage button & parameters
button2 = Buttons.Button(screen, screenSize / 2, screenSize / 2 - 50, 150, 40, WHITE, GREY, BLUE, textcolour=BLACK,
                 textcolour2=BLACK, TEXT="Start")
button3 = Buttons.Button(screen, screenSize / 2, screenSize / 2, 150, 40, WHITE, GREY, BLUE, textcolour=BLACK,
                 textcolour2=BLACK, TEXT="Settings")
button4 = Buttons.Button(screen, screenSize / 2, screenSize / 2 + 50, 150, 40, WHITE, GREY, BLUE, textcolour=BLACK,
                 textcolour2=BLACK, TEXT="Quit")
startButtons = [button2, button3, button4]
#endregion
#endregion

#parameters below control which page we are currently on
runPage = False
setPage = False
startPage = True


#controls framerate per second
fps = 100

#the values below set the parameters for the size and position of grid and cells.


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
        # start the simulation
        if button1.leftClicked():
            setPage = False
            runPage = True
            fps = 3
        #increase the gridSize
        elif button6.leftClicked() and watchCounter <= 0:
            watchCounter = 10
            gridSize += 1
            if gridSize == 10:
                gridSize = 0
            setSizeChange(gridSize)
        #decrease the gridSize
        elif button5.leftClicked() and watchCounter <= 0:
            watchCounter = 10
            gridSize -= 1
            if gridSize == -1:
                gridSize = 9
            setSizeChange(gridSize)
        #centralize
        elif button7.leftClicked() and watchCounter <= 0:
            newMatrix.centralize()
            watchCounter = 20
        watchCounter -= 1
        pygame.display.update()
        

    elif startPage:
        startUpdateDraw()
        if button2.leftClicked():
            setPage = True
            startPage = False
            pygame.time.delay(100)
            newMatrix = Main.GOLMatrix(1,1)
            setSizeChange(gridSize)

